# Development Apps

These are apps that are useful for developers of home portal or the home portal component libraries.

The following apps are included in this category:

- Home Portal Component Library Storybook
- API Coverage Report

These apps are available for `v0.2.0` and above.

If you would like to have these apps included, follow the below steps:

## 1. Shut down the home portal

You will need to shut down the home portal to install these apps. To do this, run the following command:

```bash
docker-compose down
```

## 2. Update the caddyfile

You will need to update the `Caddyfile` to include the new apps. Add the following snippet to the `Caddyfile` close to the already existing rules:

```caddy
handle_path /dev/coverage/api/* {
    root * /var/www/html/coverage/hp/api/
    file_server
}

handle_path /components/* {
    root * /var/www/html/components/
    file_server
}
```

These static files are already available on the home portal image, so the above snippet will serve them.


## 3. Start home portal

Now that you have updated the `Caddyfile`, you can start the home portal again by running the following command:

```bash
docker-compose up -d
```

## 4. Run the script for the apps to be registered

You can run the script using the following command:

```bash
./scripts/development.sh
```

This script will create rows for the new apps so that they are available on the home portal landing page.

## Additional Information

You can access the applications records by visting the home portal admin page.

The name of these applications are:

- Home Portal Storybook
- Coverage Report - API

There is also a category that gets created called alongside these apps called `Development`.