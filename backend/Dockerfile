FROM python:3.9.18-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/
COPY ./ app/backend/
CMD ["uvicorn", "backend.main:app","--host","0.0.0.0", "--reload", "--port=8000"]