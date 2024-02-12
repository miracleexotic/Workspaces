# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /backend

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]
