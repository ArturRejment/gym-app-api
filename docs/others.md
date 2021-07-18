# Other Endpoints

## Working hours


### `workingHours/`
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

## Address


### `address/`
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


## Shop

### `shop/`
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


## Product

### `product/`
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


### `product/viewProducts`
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


### `product/addProductToShop`
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


## Membership

### `membership/`
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


### `membership/activeMemberships`
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


### `membership/renewMemberships`
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


## Group Training

### `groupTraining/`
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


### `groupTraining/signForTraining`
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