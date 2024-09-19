.PHONY: clean static requirements format lint test db dev down migrations migrate superuser init

clean:
	rm -rf .mypy_cache \
	**/__pycache__ \
	**/**/__pycache__ \
	.coverage \
	.pytest_cache \
	build/ \
	dist/ \
	*.egg-info \
	coverage.xml \
	htmlcov \
	runtime.log \
	debug.log

static:
	@rm -rf static/
	@python manage.py collectstatic --no-input

requirements:
	pipenv requirements > requirements.txt
	pipenv requirements --dev > requirements.dev.txt

format:
	black .
	isort . --profile black

lint:
	black --check .
	isort . --check-only --profile black
	flake8 . --max-line-length=100
	mypy . --strict

test:
	pytest . --cov=. --no-cov-on-fail --cov-report term-missing
	coverage xml
	coverage html

db:
	docker compose -f compose.dev.yaml up -d

dev:
	python manage.py runserver

down:
	docker compose -f compose.dev.yaml down

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

init:
	python manage.py iapps
