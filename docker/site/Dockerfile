FROM python:3.12.4-alpine3.20 AS backend

COPY backend/requirements.dev.txt /build/install/
WORKDIR /build/install
RUN pip install -r requirements.dev.txt

COPY backend/ /build/backend/
WORKDIR /build/backend
RUN pytest . --cov=. --no-cov-on-fail --cov-report term-missing && coverage html

FROM python:3.12.4-alpine3.20 AS docs

COPY docs/requirements.txt /build/install/
WORKDIR /build/install

RUN pip install -r requirements.txt

COPY docs/ /build/docs/
WORKDIR /build/docs

RUN mkdocs build

FROM node:20.16.0-alpine3.20 AS components

COPY packages/components/ /build/components
WORKDIR /build/components

RUN npm ci && npm run storybook:build

FROM caddy:2.8.4-alpine AS shopping
WORKDIR /shopping/

RUN apk add --no-cache wget unzip zip

RUN wget https://github.com/Evanlab02/ShoppingListApp/releases/download/v0.16.3/frontend.zip
RUN unzip frontend.zip

RUN wget https://github.com/Evanlab02/ShoppingListApp/releases/download/v0.16.3/static.zip
RUN unzip static.zip

FROM caddy:2.8.4-alpine

COPY backend/static /var/www/html/static
COPY frontend/dist/ /var/www/html/site/
COPY --from=docs /build/docs/site/ /var/www/html/docs/
COPY --from=components /build/components/storybook-static/ /var/www/html/components/
COPY --from=backend /build/backend/htmlcov/ /var/www/html/coverage/hp/api/

COPY --from=shopping /shopping/dist/ /var/www/html/shopping/site/
COPY --from=shopping /shopping/backend/static/ /var/www/html/shopping/static/

EXPOSE 80
EXPOSE 9999
