# Home Portal Component Library

This is the home portal component library. It is a collection of reusable components that can be used to build the home portal or apps that will live within the home portal.

If you are developing an application that will solely live within the home portal, you should use consider using these components to ensure a consistent look and feel however if your application will be used in and outside of the home portal feel free to use whatever components you like. This is not a requirement to integrate with home portal.

## Pre-requisites

- Node.js (v20.16.0)
- npm (10.8.1)

## Getting started

You can install the dependencies by running:

```bash
npm install
```

To start the storybook, run:

```bash
npm run storybook
```

## Other commands

### Testing

To run the tests:

```bash
npm run test
```

To update snapshots for the tests:

```bash
npm run test:update
```

### Linting

To run the linter:

```bash
npm run lint
```

To fix linting issues:

```bash
npm run lint:fix
```

### Build

To build the application:

```bash
npm run build
```