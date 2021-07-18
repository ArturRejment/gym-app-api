# Authorization

Authorization for this project is provided by Djoser https://djoser.readthedocs.io/en/latest/introduction.html

## API Endpoints for Authorization

### `auth/users/me/`
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

### `auth/token/login/`
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

### `auth/users/`
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

### `auth/token/logout/`
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