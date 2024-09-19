# Home Portal FE

This is the home for the home portal front end. This is a React application that is used to display the home portal.

## Pre-requisites

- Node.js (v20.16.0)
- npm (10.8.1)

## Getting started

You can install the dependencies by running:

```bash
npm install
```

To start the application, run:

```bash
npm run dev
```

### Disclaimer

The application relies on there being a backend service running on `http://localhost:80`. If you are running the backend service on a different port, you will need to update the `vite.config.ts` file to reflect the correct port.

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