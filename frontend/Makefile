.PHONY: refresh dev format lint clean

clean:
	rm -rf coverage dist html

refresh:
	npm install ../packages/components/index.tgz

dev:
	npm run dev

format:
	npm run lint:fix

lint:
	npm run lint