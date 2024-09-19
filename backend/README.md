# Home Portal Backend

This is the home for the home portal backend. This is a Django project that serves as the backend for the home portal.

## Getting started

Find below the steps to get started with the project.

### Pre-requisites

Pre-requisites:
- Python 3.12
- Pipenv
- Docker
- Docker compose

Clone the repository and install the dependencies:

```bash
pipenv install --dev
```

You should also take a look at `.env.template` and create a `.env` file with the required environment variables.

### Running the development server

To start the development database, we use docker compose:

```bash
docker compose -f compose.dev.yaml up -d

# To turn it off
docker compose -f compose.dev.yaml down
```

You will need to run the migrations:

```bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```

You can create a superuser to access the admin panel:

```bash
pipenv run python manage.py createsuperuser
```

And you can do the initial data load:

```bash
pipenv run python iapps
```

Finally, to start the development server, run:

```bash
pipenv run python manage.py runserver
```

The development server should now be running on `http://localhost:8000`.

## Checks

Find below all the checks that will be done when opening a PR (All these are runnable locally):

### Linting and type checking

To lint and type check the code, run:

```bash
pipenv run black --check .
pipenv run isort . --check-only --profile black
pipenv run flake8 . --max-line-length=100
pipenv run mypy . --strict
```

### Tests and coverage

To run the tests and generate coverage, run:

```bash
pipenv run pytest . --cov=. --no-cov-on-fail --cov-report term-missing
pipenv run coverage xml
pipenv run coverage html
```

## Other important commands

### Generating requirements

You should generate the requirements file after installing or updating a package:

```bash
pipenv requirements > requirements.txt
pipenv requirements --dev > requirements.dev.
```

### Generating static files

To generate the static files, run:

```bash
pipenv run python manage.py collectstatic --no-input
```

### Disclaimer

Please note these commands need to be run when updating requirements or static files. This is used in the pipeline to generate the artifacts.
