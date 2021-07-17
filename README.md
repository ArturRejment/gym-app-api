# Gym App API
An API for Gym App built with Django and REST Framework. User authentication is provided by Djoser.
This API provides endpoints from which you can fetch the data for your front-end application.

- [How to run the server?](#how-to-run-the-server)
  - [With Docker](#with-docker)
  - [Without Docker](#without-docker)
  - [Manage the database](#manage-the-database)
  - [Testing](#testing-with-docker)
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
- [Working hours](#working-hours)
  - [`workingHours/`](#workinghours)
- [Address](#Address)
  - [`address/`](#address)
- [Shop](#Shop)
  - [`shop/`](#shop)
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

## Manage the database
If you want to manage your database, create a superuser and go to the admin page.

- If you use Docker open gymserver with bash: `docker exec -it gym-app-server bash` and type `python manage.py createsuperuser`
- If not, make sure you have virtual env active, open directory where is `manage.py` file and type `python manage.py createsuperuser`
- Provide the required informations like username, email, password etc.
- Run the server, go to the `http://127.0.0.1:8000/admin` and log in with credentials provided in the previous step

## Testing

To run the tests while using Docker open gymserver with bash: `docker exec -it gym-app-server bash` and type `python manage.py test`

If you're not using Docker make sure you have virtual env active and type `python manage.py test`



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

# Working hours

## `workingHours/`
- Allowed methods
 - [x] GET
 - [x] POST
 - [ ] DELETE

- Allowed roles
  - [ ] Member
  - [x] Trainer
  - [x] Receptionist

`GET` allows to browse all working hours

`POST` allows to create new working hour
Parameters send with request:
- start_time
- finish_time
# Address

## `address/`
- Allowed methods
 - [x] GET
 - [x] POST
 - [ ] DELETE

- Allowed roles
  - [x] Member (POST)
  - [x] Trainer (POST)
  - [x] Receptionist (POST, GET)

`GET` allows to view all addresses
Parameters send with request:
- None

`POST` allows to create new address
Parameters send with request:
- country
- city
- street
- postcode

# Shop
## `shop/`
- Allowed methods
  - [x] GET
  - [x] POST
  - [x] DELETE

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

`DELETE` allows to delete shop managed by logged receptionist

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
  - [x] DELETE

- Allowed roles
  - [x] Member (GET)
  - [x] Trainer (GET)
  - [x] Receptionist (GET, POST, DELETE)

`GET`
allows to browse all the memberships

Parameters send with request:
- None

`POST`
allows to create new membership
Parameters send with request:
- membership_type
- membership_price

`DELETE` allows to delete membership specified by id
Parameters to send with request:
- membershipID

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
  - [x] DELETE

- Allowed roles
  - [x] Member (GET)
  - [x] Trainer (GET)
  - [x] Receptionist (GET, POST, DELETE)

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

`DELETE` allows to delete group training specified by id
Parameters send with request:
- trainingID

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




