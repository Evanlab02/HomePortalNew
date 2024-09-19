# Post Setup

After you have started home portal, there is nothing more for you to do, however below we will provide you with some information on how you can further customize your home portal.

## Introduction

The home portal is a collection of docker containers that creates a one in all solution for your home management needs. The home portal is built on top of Django and React, and uses PostgreSQL as the database. The home portal is designed to be a self-hosted solution that you can run on your own hardware at home.

## Customizing the home portal

You can add applications to home portal by following our guides on each application. You can also attempt to add your own application to home portal. If you would like to add your application to the officially supported applications, please reach out to me @ [evanlabuschagne70@gmail.com](mailto:evanlabuschagne70@gmail.com).

We will not go into detail on how to add applications to home portal here but we will discuss the different parts of this process.

### Compose files

The home portal is built on top of docker and uses docker-compose to manage the containers. You can add your own applications to the home portal by adding a new service to the `docker-compose.yml` file. 

There is not much here to detail except that you should make sure that when you add your service to the `docker-compose.yml` file, you should ensure it matches what we detail in our guides.

### Caddyfile

The Caddyfile is the configuration file for the Caddy server that is used to serve the home portal static files.

This is where you can expose some static files that come with the home portal image to enable different apps. To do so, follow an application setup guide and ensure that you add the necessary configuration to the Caddyfile as detailed in the guide.

NOTE: You could also add your own static files by creating your own custom image on top of the home portal image. Please note this is not fully recommended as it could break the home portal or override some of the home portal static files however it is possible to do so. This will also require you to update the compose file to match your custom image. In future we will have a guide for this.

### Admin panel and application settings

The home portal comes with an admin panel that you can use to manage the applications that are installed on the home portal. You can access the admin panel by going to `http://localhost:8000/admin/` and logging in with the superuser credentials you created during the setup process.

Please note that there are application settings that you can change in the admin panel, that allow you to change the link that the application is served on, the name of the application in the interface, icon and more. This should not be changed often as this will most of the time require you to change several configurations in the Caddyfile and the compose file.

You might be wondering, why provide this functionality if it so complex? The reason this exists is some applications we integrate into the home portal do not rely on the fact that it is running as part of the compose stack so it could be hosted anywhere or change where it is hosted and you should have the ability to change the link that the application is served on.

This also allows for easy integration into things you might already be running on your network. Please refer to the application guides to see if it is recommended to change the application settings, this will definitely be needed in some cases and those guides will be the best place to find that information.

### Environment variables

We use `.env` files to manage the environment variables that are used in the home portal. You can add your own environment variables to the `.env` file to customize the home portal.

Please note that these .env files are often crucial to the home portal. Please ensure to closely follow the application guides when adding environment variables to the `.env` file to ensure your apps work correctly.
