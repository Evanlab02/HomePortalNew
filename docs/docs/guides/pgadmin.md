# PgAdmin

You will need to setup up PgAdmin to read from the home portal database. This will allow you to view the data in the database and make changes to it.

## 1. Access PgAdmin

To access PgAdmin, you will need to navigate to the following URL in your browser:

```bash
http://<your_host_name>/pgadmin/
```

## 2. Login to PgAdmin

You will need to login to PgAdmin using the credentials you setup in your .env file.

## 3. Register the Home Portal Database

Right click on servers and select `Register --> Server`. You will need to fill in the following details:

- General --> Name: `Home Portal Database`
- General --> Ensure `Connect Now` is checked
- Connection --> Host name/address: `hp-postgres-16`
- Connection --> Username: `<your_home_portal_db_user>`
- Connection --> Password: `<your_home_portal_db_password>`
- Connection --> Ensure `Save password` is checked

Click save and you should now be able to view the home portal database.
