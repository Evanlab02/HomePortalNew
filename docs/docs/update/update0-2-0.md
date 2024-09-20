# Update Guide for 0.2.0

## Introduction

This guide is intended to help you update your project from version 0.1.0 to 0.2.0. It will guide you through the changes that need to be made in order to update your project.

## Update Steps

This is simple update, you will need to update all your tags in your compose file to the new version (v0.2.0) along with one other thing.

We now expose another port on caddy, so you will need to update your caddy service to expose the new port.

```yaml	
  home-portal-site:
    container_name: hp-site
    image: ghcr.io/evanlab02/hp-site:v0.2.0
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

If you want the exact snippet to copy paste, here it is:

```yaml
    expose:
      - 80
      - 9999
    ports:
      - "80:80"
      - "9999:9999"
```