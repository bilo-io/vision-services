FROM python:3.12.3-slim-bullseye


WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8000

ENV APP_WORKERS=${APP_WORKERS:-1}

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers ${APP_WORKERS}