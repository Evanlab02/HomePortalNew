.PHONY: s-pull s-build s-debug s-up s-down s-fresh superuser pull debug up down

sync:
	cd ./packages/components/ && npm install && make build
	cp ./packages/components/index.tgz ./frontend/index.tgz
	mv ./frontend/index.tgz ./frontend/components.tgz
	cd ./frontend/ && npm install

s-pull:
	docker compose -f compose.staging.yaml pull

s-build:
	cd ./frontend/ && npm install && npm run build
	docker compose -f compose.staging.yaml build
	docker image prune -f

s-debug:
	docker compose -f compose.staging.yaml up

s-up:
	docker compose -f compose.staging.yaml up -d

s-down:
	docker compose -f compose.staging.yaml down

s-fresh: s-build s-pull 
	docker compose -f compose.staging.yaml up

superuser:
	docker exec -it hp-admin python manage.py createsuperuser

pull:
	docker compose pull

debug:
	docker compose up

up:
	docker compose up -d

down:
	docker compose down