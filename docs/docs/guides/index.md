# Setting up

This guide will take you through setting up home portal on your local machine. 

## Prerequisites

To get started with home portal, you will need to have the following installed on your machine:

- Docker
- Docker Compose
- Home Portal Files

## 1. Setup your environment

Create a `.env` file in the root of the home portal directory and add the following environment variables:

```bash
# POSTGRES CONFIG
POSTGRES_PASSWORD=<password_of_your_choosing>
POSTGRES_DB=home-portal-db

# PGADMIN CONFIG
PGADMIN_DEFAULT_EMAIL=<email_of_your_choosing>
PGADMIN_DEFAULT_PASSWORD=<password_of_your_choosing>

# HOME PORTAL CONFIG
HP_API_DJANGO_KEY=somethinglongerthan50charactersthatcontainsatleast1number
HP_API_DJANGO_HOST=<yourhostname>
HP_API_DATABASE_PASSWORD=<password_of_your_choosing>
HP_API_DB_HOST=hp-postgres-16
# Optional
# HP_API_DJANGO_HOST_ALT=<yourhostname>
# HP_API_DJANGO_HOST_ALT2=<yourhostname>
```

## 2. Start the services/containers

To start the services/containers, you will need to run the following command:

```bash
docker-compose up -d
```

If you have not named the compose file the standard name, you will need to specify the file name:

```bash
docker-compose -f <file-name> up -d
```

## 3. Run the install script

The install script does two things:

1. It creates a super user for the home portal so that you can access the admin panel.
2. It creates the default applications that come with the home portal.

To run the install script, you will need to run the following command:

```bash
./scripts/install.sh
```

## 4. Access the home portal

You will now be able to access the home portal by going to the following URL:

```bash
http://<yourhostname>:80
```
