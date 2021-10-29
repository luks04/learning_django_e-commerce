# learning_django_e-commerce

> Note: Django release notes:    https://docs.djangoproject.com/en/3.2/releases/

## Manage actions
- To create the Django project
```sh
django-admin startproject my_ecommerce_project
```
- To run the app
```sh
python3 manage.py runserver
```
- To create an internal app
```sh
python3 manage.py startapp <app_name>
```
- To generate the SQL code (after editing the models)
```sh
python3 manage.py makemigrations
```
- To create all the fields on the admin (after executing 'makemigrations')
```sh
python3 manage.py migrate
```
- To create the super user to be able to access to the admin
```sh
python3 manage.py createsuperuser
```