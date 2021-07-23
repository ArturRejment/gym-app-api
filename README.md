# Gym App API
An API for Gym App built with Django and REST Framework. User authentication is provided by Djoser.
This API provides endpoints wherefrom you can fetch the data for your front-end application.

- [How to run the server?](#how-to-run-the-server)
  - [With Docker](#with-docker)
  - [Without Docker](#without-docker)
  - [Testing](#testing)
- [Set up project](#set-up-project)
- [Testing](#testing)


# How to run the server

## With Docker
- Set the project with `docker-compose run gymserver`
- Run servers with `docker-compose up`
- To migrate the database open gymserver with bash: `docker exec -it gym-app-server bash` and type `python manage.py migrate`

You can build the project with `docer-compose build`

## Without Docker
- Clone this repo
- Create Postgres DB locally
- Go to the Django project settings: `backend > settings.py`
- Find `DATABASES` dictionary and change db credentials to match with yours
- Create virtual environment with command `python -m venv env`
- Type `env\Scripts\activate.bat` to activate the environment
- Type `pip install -r requirements.txt` to install all the necessary libs
- Set the database with `python manage.py migrate`
- Run server with `python manage.py runserver`

## Set up project

Now you can set up project by [following this doc](https://github.com/ArturRejment/gym-app-api/blob/main/docs/project_set_up.md)

## Testing

In order to run the tests with Docker, open gymserver with bash: `docker exec -it gym-app-server bash` and type `python manage.py test`

If you're not using Docker make sure you have virtual env active and type `python manage.py test`







