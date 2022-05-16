# c2cLoanBank
 
 This webapp solves the issue of lending and getting loan from general public instead of a public entity like banks or finance companies.
 
### Tech Stack
  Frontend - HTML,CSS,JS
  Backend - Django
  Database - Postgresql
  
### Basic Requirement
  Install python in ur system
  Install postgresql,pgadmin and connect both.

### Steps to link database with project
- install postgresql and pgadmin 
- connect both with same port for example:port 5432
- while opening pgadmin it will ask for password .whether you create on  your own or use my password january27
- create database at pgadmin and fill username ,host name .
- fill localhost at hostname
- to link pgadmin with project do the following changes in *setting.py* 
```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': ‘<database_name>’,
       'USER': '<database_username>',
       'PASSWORD': '<password>',
       'HOST': '<database_hostname_or_ip>',
       'PORT': '<database_port>',
   }
}
```
#### For Example my code has this setup
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  'lcoloans',
        'USER':'postgres',
        'PASSWORD':'january27',
        'HOST':'localhost'
    }
}
```

### Steps to run in local

- git clone
- pipenv shell
- pipenv install
- pipenv install django-crispy-forms
- cd loan/loanbank
- python manage.py runserver
