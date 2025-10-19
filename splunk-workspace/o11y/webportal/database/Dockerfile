# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /backend

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

RUN opentelemetry-bootstrap -a install

COPY . .
EXPOSE 8000
CMD ["opentelemetry-instrument" ,"uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "./Certs/cert.key", "--ssl-certfile", "./Certs/cert.crt"]
