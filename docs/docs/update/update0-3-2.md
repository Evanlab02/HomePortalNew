# Update Guide for 0.3.2

## Introduction

This guide is intended to help you update your project from version 0.2.0 to 0.3.2. It will guide you through the changes that need to be made in order to update your project.

### Get ready for a new look and feel of documentation

We have updated the way the docs look and feel, this should not be too much of an adjustment, but worthwhile to put here.

### Upgrading images to 0.3.2

The most simple step is to upgrade all the home portal images to `v0.3.2`.

```yaml
  home-portal-admin:
    container_name: hp-admin
    image: ghcr.io/evanlab02/hp-admin:v0.3.2
    env_file:
      - .env
    depends_on:
      home-portal-postgres-16:
        condition: service_healthy
    restart: always
    networks:
      - home-portal-network
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
    command: "/bin/bash -c 'python manage.py migrate && uvicorn hub.admin.asgi:application --host 0.0.0.0 --port 80 --workers 1'"

  home-portal-api:
    container_name: hp-api
    image: ghcr.io/evanlab02/hp-api:v0.3.2
    env_file:
      - .env
    depends_on:
      home-portal-postgres-16:
        condition: service_healthy
    restart: always
    networks:
      - home-portal-network
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M

  home-portal-site:
    container_name: hp-site
    image: ghcr.io/evanlab02/hp-site:v0.3.2
    env_file:
      - .env
    restart: always
    expose:
      - 80
      - 9999
    ports:
      - "80:80"
      - "9999:9999"
    networks:
      - home-portal-network
    volumes:
      - ./site/Caddyfile:/etc/caddy/Caddyfile
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
```

### Update Shopping List App to 0.17.0 if you are using it

Now officially support and recommend version `0.17.0` of the Shopping List App. Please review the [changelog](https://github.com/Evanlab02/ShoppingListApp/releases/tag/v0.17.0) for the Shopping List App on its repository.

**NOTE: You should also review the changelog for all versions between `0.16.2` and `0.17.0`. These are mostly behind the scene improvements, that are easy to start using with this upgrade.**

```yaml
  shopping-django-administration:
    container_name: shopping-django-admin
    image: ghcr.io/evanlab02/shoppingappadmin:0.17.0
    env_file:
      - .env
    environment:
      SHOPPING_DEFAULT_SETTINGS_MODULE: shoppingapp.settings.settings
    command: /bin/bash -c "python manage.py migrate && python manage.py runserver"
    depends_on:
      home-portal-postgres-16:
        condition: service_healthy
    networks:
      - home-portal-network
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M

  shopping-django-app:
    container_name: shopping-django-app
    image: ghcr.io/evanlab02/shoppingappbe:0.17.0
    environment:
      SHOPPING_DEFAULT_SETTINGS_MODULE: shoppingapp.settings.settings
    env_file:
      - .env
    command: "gunicorn -b 0.0.0.0:80 -w 1 --log-config shoppingapp/logging.config --capture-output --log-level info --worker-class uvicorn_worker.UvicornWorker 'shoppingapp.config.asgi:app'"
    depends_on:
      home-portal-postgres-16:
        condition: service_healthy
    networks:
      - home-portal-network
    restart: always
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
```
