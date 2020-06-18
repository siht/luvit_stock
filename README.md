# Backend Challenge

This app intends to be an REST API that insert and shows products.

## DEPENDENCIES

- python 3.8.3
- list of dependencies comes in requirements.txt
- optional a database like mariabd or postgres if you want to put this in production

### ENVIRONMENT VARIABLES

- SECRET_KEY
- DEBUG
- DEFAULT_DB
- ALLOWED_HOSTS
- LANGUAGE_CODE
- TIME_ZONE
- USE_I18N
- USE_L10N
- USE_TZ
- STATIC_URL
- STATIC_ROOT

can you set with a .env file, only put that file under stock_project directory, [read why](https://django-environ.readthedocs.io/en/latest/).

## HOW TO INSTALL

run inside this project

```sh
pip install -r requirements.txt
```

for install dependencies

after set all environment variables

run with db running

```sh
./manage.py migrate
```

run also this command and remember your credentials

```sh
./manage.py createsuperuser
```

## HOW TO RUN

### DEVELOPMENT

after that you have installed and configured only left run

```sh
./manage.py runserver
```

### PRODUCTION

also you need to install via pip some server that understand wsgi python protocol I suggest use gunicorn or wsgi read in [django documentation](https://docs.djangoproject.com/en/3.0/howto/deployment/) about.

## RUN TESTS

```sh
./manage.py test
```

for run tests

## ROUTES

- GET /api/products/
- POST /api/products/bulk_insert/

try with curl (you must have a superuser created, see how to install section), for post products, see INSTRUCTIONS.md

```sh
curl -H "Content-Type: application/json" -X POST -u <your-username>:<your-password> --data '{"products": [{"id": "abc123", "name": "some", "value": 99.9, "discount_value": 10, "stock": 1000}]}' http://your-host:your-port/api/products/bulk_insert/
```

to check your products

```sh
curl -H "Content-Type: application/json" http://your-host:your-port/api/products/
```
