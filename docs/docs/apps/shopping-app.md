# Shopping App

This is a shopping app that allows users to manage their shopping lists within their household via the home portal.
Please feel free to check out the repository [here](https://github.com/Evanlab02/ShoppingListApp).

NOTE: This app is only available for ``v0.1.0`` and above.
NOTE: This app can not run on the default port of the home portal and will require another port to be used. (Port 9999)

Follow the below steps to get it set up:

## 1. Update your .env file

You will need to update your `.env` file to include the following:

```bash
# SHOPPING APP CONFIG
SHOPPING_DJANGO_KEY=<somethinglongerthan50charactersthatcontainsatleast1number>
SHOPPING_DJANGO_HOST=<the_host_you_want_to_use>
SHOPPING_DATABASE_NAME=shopping-db
SHOPPING_DATABASE_USER=<your_home_portal_db_user>
SHOPPING_DATABASE_PASSWORD=<your_home_portal_db_password>
SHOPPING_DB_HOST=hp-postgres-16
SHOPPING_DB_PORT=5432
SHOPPING_DEFAULT_SETTINGS_MODULE=shoppingapp.settings.settings
```

## 2. Create the database

You will need to use provided pgadmin interface that comes along with the home portal to create the database.

NOTE: If you have not already, please check out the [PgAdmin guide](../guides/pgadmin.md) to setup the connection between PgAdmin and the home portal database.

Use your home portal database user for the new database and name the new database: `shopping-db` (Or if you changed it in the `.env` file, use that name).

NOTE: It is not recommended to change the database name from `shopping-db`.

## 3. Shut down the home portal and change the compose file

You will need to shut down the home portal and change the `compose.yml` file to include the shopping app.

Find below a snippet of what you need to add:

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

## 4. Update the caddyfile

Add the following to your caddyfile:

```
:9999 {
	handle_path /* {
    	reverse_proxy shopping-django-app:80
	}

	handle_path /apis/shopping/* {
    	reverse_proxy shopping-django-app:80
	}

	handle_path /static/* {
		root * /var/www/html/shopping/static/
		file_server
	}

	handle_path /shopping/dashboard/* {
    	root * /var/www/html/shopping/site/
    	file_server
	}
}
```

## 5. Start home portal and setup the app

You will now want to start the home portal again using the following command:

```bash
docker-compose up -d
```

You will then want to run the installation script using the following command:

```bash
./scripts/shopping.sh
```

This will create your super user for the shopping app admin page and install the app onto the home portal database.

## Disclaimer

The install script assumes the Shopping List App is living at `http://localhost:9999`. If you are using a different port or host, you will need to update this within the home portal admin page for the Shopping List App entry and Shopping List App Admin entry.
