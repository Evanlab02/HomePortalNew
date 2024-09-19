FROM python:3.12.4-alpine3.20

RUN apk add --no-cache bash

COPY version.txt /app/version.txt
COPY backend/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY backend/hub /app/hub
COPY backend/apps/ /app/apps/

EXPOSE 80

ENTRYPOINT [ "uvicorn" ]
CMD [ "hub.servers.asgi:application", "--host", "0.0.0.0", "--port", "80", "--workers", "4" ]