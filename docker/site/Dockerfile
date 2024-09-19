FROM python:3.12.4-alpine3.20 AS backend

COPY backend/ /build/backend/
WORKDIR /build/backend

RUN pip install -r requirements.dev.txt
RUN pytest . --cov=. --no-cov-on-fail --cov-report term-missing && coverage html

FROM python:3.12.4-alpine3.20 AS docs

COPY docs/ /build/docs/
WORKDIR /build/docs

RUN pip install -r requirements.txt
RUN mkdocs build

FROM node:20.16.0-alpine3.20 AS components

COPY packages/components/ /build/components
WORKDIR /build/components

RUN npm ci && npm run storybook:build

FROM caddy:2.8.4-alpine

COPY backend/static /var/www/html/static
COPY frontend/dist/ /var/www/html/site/
COPY --from=docs /build/docs/site/ /var/www/html/docs/
COPY --from=components /build/components/storybook-static/ /var/www/html/components/
COPY --from=backend /build/backend/htmlcov/ /var/www/html/coverage/hp/api/

EXPOSE 80