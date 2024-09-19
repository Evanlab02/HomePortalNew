.PHONY: clean build format lint storybook dev

clean:
	rm -rf lib
	rm -rf hp-react-components.tgz
	rm -rf dist/
	rm -rf coverage
	rm -rf html

build: clean
	rm -rf index.tgz
	npm run build
	npm pack
	mv *.tgz index.tgz

format:
	npm run lint:fix

lint:
	npm run lint

storybook:
	npm run storybook:build

dev:
	npm run storybook
	