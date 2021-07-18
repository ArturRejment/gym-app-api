# Trainer

## API Endpoints

### `trainer/working/`
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

### `viewActiveHours/`
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

### `trainer/viewGroupTrainings/`
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

### `signForPersonalTraining/`
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