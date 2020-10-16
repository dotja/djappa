# djappa

A Django project configured to be deployed to AWS Lambda with Zappa.

This repo contains the skeleton for a Django project that uses S3 for static file storage as well as a PostgreSQL backend.
The `zappa_settings.json` file contains the variables that need to be defined for a serverless deployment.

## Usage

* `zappa init`
* `zappa deploy dev`
* `zappa update dev`
