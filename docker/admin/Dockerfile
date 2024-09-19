FROM python:3.12.4-alpine3.20

RUN apk add --no-cache bash

COPY version.txt /app/version.txt
COPY backend/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY backend/hub /app/hub
COPY backend/apps/ /app/apps/
COPY backend/manage.py /app/manage.py

EXPOSE 80
