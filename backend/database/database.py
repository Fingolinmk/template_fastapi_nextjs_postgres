from sqlmodel import SQLModel, create_engine

database_url = "postgresql://user:password!@db/database" # TODO -> Move to env variable
connection_args={}
engine = create_engine(database_url, echo=True, connect_args=connection_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
