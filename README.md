# Gym App API
An API for Gym App built with Django and REST Framework. User authentication is provided by Djoser.
This API provides endpoints from which you can fetch the data for your front-end application.

- [How to run the server?](#how-to-run-the-server)
  - [View the database](#view-the-database)
- [Authentication](#Authentication)
  - [`auth/users/me/`](#authusersme)
  - [`auth/token/login/`](#authtokenlogin)
  - [`auth/users/`](#authusers)
  - [`auth/token/logout/`](#authtokenlogout)
- [Trainer](#Trainer)
  - [`trainer/working/`](#trainerworking)
  - [`viewActiveHours/`](#viewactivehours)
  - [`trainer/viewGroupTrainings/`](#trainerviewgrouptrainings)
  - [`signForPersonalTraining/`](#signforpersonaltraining)
- [Shop](#Shop)
  - ['shop/`](#shop)
- [Product](#Product)
  - [`product/`](#product)
  - [`product/viewProducts`](#productviewproducts)
  - [`product/addProductToShop`](#productaddproducttoshop)
- [Membership](#Membership)
  - [`membership/`](#membership)
  - [`membership/activeMemberships`](#membershipactivememberships)
  - [`membership/renewMembership`](#membershiprenewmembership)
- [Group Training](#Group-training)
  - [`groupTraining/`](#grouptraining)
  - [`groupTraining/signForTraining/`](#grouptrainingsignfortraining)


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

# Shop
## `shop/`
- Allowed methods
  - [x] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [ ] Trainer
  - [x] Receptionist

`GET`
allows to view all shops

Parameters send with request:
- None

`POST`
allows create a new shop

Parameters send with request:
- address
- shop_name

# Product
## `product/`
- Allowed methods
  - [x] GET
  - [x] POST
  - [x] DELETE

- Allowed roles
  - [ ] Member
  - [ ] Trainer
  - [x] Receptionist

`GET`
allows to view all available products in the storage

Parameters send with request:
- None

`POST`
allows to create a new product

Parameters send with request:
- product_name
- product_price
- product_weight

`DELETE`
allows delete particular product

Parameters send with request:
- shopProduct

## `product/viewProducts`
- Allowed methods
  - [x] GET
  - [ ] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [x] Trainer
  - [x] Receptionist

`GET`
allows to view products available in particular shop

Parameters send with request:
- shopID

## `product/addProductToShop`
- Allowed methods
  - [ ] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [ ] Trainer
  - [x] Receptionist

`POST`
allows to add product to the shop

Parameters send with request:
- amount
- productID

# Membership
## `membership/`
- Allowed methods
  - [x] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member (GET)
  - [x] Trainer (GET)
  - [x] Receptionist (GET, POST)

`GET`
allows to browse all the memberships

Parameters send with request:
- None

`POST`
allows to create new membership
Parameters send with request:
- membership_type
- membership_price

## `membership/activeMemberships`
- Allowed methods
  - [x] GET
  - [ ] POST
  - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [ ] Trainer
  - [x] Receptionist

`GET`
allows to browse all the active memberships

Parameters send with request:
- None

## `membership/renewMemberships`
- Allowed methods
  - [ ] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [ ] Trainer
  - [ ] Receptionist

`POST`
allows to renew membership

Parameters send with request:
- membershipID

# Group Training
## `groupTraining/`
- Allowed methods
  - [x] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member (GET)
  - [x] Trainer (GET)
  - [x] Receptionist (GET, POST)

`GET`
allows to browse all the group trainings

Parameters send with request:
- None

`POST`
allows to create new group training

Parameters send with request:
- training_name
- trainer
- time
- max_people

## `groupTraining/signForTraining`
- Allowed methods
  - [ ] GET
  - [x] POST
  - [ ] DELETE

- Allowed roles
  - [x] Member
  - [ ] Trainer
  - [ ] Receptionist

`POST`
allows to sign for group training

Parameters send with request:
- trainingID




