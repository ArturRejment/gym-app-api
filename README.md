# Gym App API
An API for Gym App built with Django and REST Framework. User authentication is provided by Djoser.
This API provides endpoints from which you can fetch the data for your front-end application.

# Endpoints

Default hostname and port: http://127.0.0.1:8000

## Valid sufixes for GET Method:

- `/auth/users/me/` [Logged user] returns details about currently logged user
- `/trainer/working/` [Trainer] returns details about trainer working hours
- `/viewActiveHours/` [Anyone] returns available training hours
- `/groupTrainings/` [Anyone] returns available group trainings
- `/viewProducts/<int:id>` [Anyone] returns products currently available in shop specified by id
- `/viewAllProducts/` [Receptionist] returns all products that can be added to the shop
- `/activeMemberships/` [Receptionist] returns every member who has active membership

## Valid sufixes for POST Method:

- `/auth/token/login/` [Anyone] allows to login for the account - returns auth_token if success
- `/auth/users/` [Anyone] allows to register an Gym Member account
- `/auth/token/logout/` [Logged user] allows to logout
- `/auth/createAddress/` [Anyone] creates an address
- `/trainer/updateHour/<int:id>/` [Trainer] allows to update information about trainer working hour specified by id
- `/signForPersonalTraining/<int:id>/` [GymMember] allows to sign for personal training specified by id
- `/signForTraining/<int:id>/` [GymMember] allows to sign for group training specified by id
- `/addProduct/<int:id>` [Receptionist] allows to add a product to the shop
- `/renewMembership/<int:id>` [GymMember] allows to renew membership

# How to run the server

- Clone this repo
- Create virtual environment with command `python -m venv env`
- Type `env\Scripts\activate.bat` to activate the environment
- Type `pip install -r requirements.txt` to install all the necessary libs
- Go to the backen location with `cd backend`
- Set the database with two commands: `python manage.py makemigrations` and then `python manage.py migrate`
- Run server with `python manage.py runserver`

## View the database
If you want to view your database, create a super user and go to the admin page.

- Open directory with `manage.py` file
- Create super user with `python manage.py createsuperuser`
- Provide the required informations like username, email, password etc.
- Run the server, go to the `http://127.0.0.1:8000/admin` and log in with credentials provided in the previous step