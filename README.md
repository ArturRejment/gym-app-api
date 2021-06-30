# Gym App API
An API for Gym App built with Django and REST Framework. User authentication is provided by Djoser.
This API provides endpoints from which you can fetch the data for your front-end application.

# Endpoints

Default hostname and port: http://127.0.0.1:8000/

# Authentication
## `auth/users/me/`
- Allowed methods
  - [x] GET
  - [ ] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [x] Trainer
  - [x] Receptionist

- GET
Returns deteils about currently logged user

Parameters send with request:
- None

## `auth/token/login/`
- Allowed methods
  - [ ] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [ ] Trainer
  - [ ] Receptionist

- POST
Allows to login, returns auth_token

Parameters send with request:
- email
- password

## `auth/users/`
- Allowed methods
  - [x] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [x] Trainer
  - [x] Receptionist

`POST`
Allows to create new member account

Parameters send with request:
- email
- password

`GET`
Returns list of all users

Parameters send with request:
- None

## `auth/token/logout/`
- Allowed methods
  - [ ] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [x] Trainer
  - [x] Receptionist

`POST`
Allows to logout, deletes auth token

Parameters send with request:
- None

# Trainer

## `trainer/working/`
- Allowed methods
  - [x] GET
  - [ ] POST
  - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [x] Trainer
  - [ ] Receptionist

`GET`
returns details about trainer working hours

Parameters send with request:
- None

## `viewActiveHours/`
- Allowed methods
  - [x] GET
  - [ ] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [x] Trainer
  - [x] Receptionist

`GET`
returns available training hours

Parameters send with request:
- None

## `trainer/viewGroupTrainings/`
- Allowed methods
  - [x] GET
  - [ ] POST
  - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [x] Trainer
  - [ ] Receptionist

`GET`
returns trainer's group trainings

Parameters send with request:
- None

## `signForPersonalTraining/`
- Allowed methods
  - [ ] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [ ] Trainer
  - [ ] Receptionist

`POST`
allows to sign for personal training specified by id

Parameters send with request:
- trainingID



- `/groupTrainings/` [Anyone] returns available group trainings
- `/viewProducts/` [Anyone] returns products currently available in shop specified by id
- `/viewAllProducts/` [Receptionist] returns all products that can be added to the shop
- `/activeMemberships/` [Receptionist] returns every member who has active membership
- `/viewMemberships/` [Anyone] returns all the memberships
- `/viewShops/` [Anyone] allows to view all shops


## Valid sufixes for POST Method:

- `/auth/createAddress/` [Anyone] creates an address
- `/trainer/updateHour/` [Trainer] allows to update information about trainer working hour specified by id
- `/signForPersonalTraining/` [GymMember]
- `/signForTraining/` [GymMember] allows to sign for group training specified by id
- `/addProduct/` [Receptionist] allows to add a product to the shop
- `/createProduct/` [Receptionist] allows to create a new product
- `/renewMembership/` [GymMember] allows to renew membership
- `/createMembership/` [Receptionst] allows to create new membership
- `/createGroupTraining/`: [Receptionist] allows to create a new group training
- `/createShop/`: [Receptionist] allows to create new shop

# How to run the server

- Clone this repo
- Create virtual environment with command `python -m venv env`
- Type `env\Scripts\activate.bat` to activate the environment
- Type `pip install -r requirements.txt` to install all the necessary libs
- Go to the backend location with `cd backend`
- Set the database with two commands: `python manage.py makemigrations` and then `python manage.py migrate`
- Run server with `python manage.py runserver`

## View the database
If you want to view your database, create a super user and go to the admin page.

- Open directory where is `manage.py` file
- Create super user with `python manage.py createsuperuser`
- Provide the required informations like username, email, password etc.
- Run the server, go to the `http://127.0.0.1:8000/admin` and log in with credentials provided in the previous step
