# Project set up

## Create superuser
After you done all the things to start the server, it's time to set up the project.
First of all, create a superuser:
- If you use Docker open gymserver with bash: `docker exec -it gym-app-server bash` and type `python manage.py createsuperuser`
- If not, make sure you have virtual env active, open directory where is `manage.py` file and type `python manage.py createsuperuser`
- Provide the required informations like username, email, password etc.

After superuser creation, go to the admin panel: http://127.0.0.1:8000/admin/ and login with credentials provided in previous steps.

## Creating new users

You should create new users with API Endpoint http://127.0.0.1:8000/auth/users/, you should not use Admin panel.
After creating a user, his default role is `member`. If you want the user to have trainer or receptionist permissions you should:
- Open Groups in Admin panel and create new Groups: `trainer` and `receptionist`
- In Admin panel open specific User and select Group that User should have
WARNING! Admin panel allows to assign more than one Group for one User, but User should have only one role (Group)

## Creating Trainers and Receptionists

If you gave trainer or receptionist permissions for the user, you should also create Trainer or Receptionist Models instances and assign User with those permissions to the instance as a one to one field relation.

## Next steps

After creating enough amout of Users, you can continue adding new things like group trainings, shops, products etc.
You can do it both from Admin panel and API Endpoints.