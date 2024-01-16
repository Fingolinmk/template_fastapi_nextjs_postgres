"""Entrypoint of the FastAPI backend """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database.database import create_db_and_tables
from backend.routes.user_route import user_route

def create_application() -> FastAPI:
    application = FastAPI(
        title="Checklist app",
        version="0.0.1",
        contact={
            "name": "Firstname Lastname",
            "email": "Firstname.Lastname@domain.com",
        },
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


def add_routes(application: FastAPI) -> FastAPI:
    tags_metadata = [
        {"name": "name", "description": "description"},
    ]
    application.openapi_tags = tags_metadata

    application.include_router(user_route)

    return application


app = create_application()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

app = add_routes(app)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
