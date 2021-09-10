# Django-React Demo
[![Build Status](https://app.travis-ci.com/allexiusw/react-crypto.svg?branch=master)](https://app.travis-ci.com/allexiusw/react-crypto)

## Clone the project

`git clone git@github.com:allexiusw/demo-crypto.git`

## WebApp

### Create the virtualenv
```
mkdir ~/.virtualenvs/
python3 -m venv ~/.virtualenvs/api
```

## Enable virtualenv
Type the following command (dudas con windows I think it is slighty different):
`. ~/.virtualenvs/api/bin/activate` 

### Run migrations
Go to the webapp path and then type the following command:
`cd api; pip install -r requirements.txt`

### Run migrations
Run migrations to do so, type the following command:
`python src/manage.py migrate`

### Create a superuser
`python src/manage.py createsuperuser`

### Run the project
To run django y dev mode:
`python src/manage.py runserver`

And then go to your localhost:8000 and you will be ready to start coding.

### Login in admin 
go to localhost:8000/admin/

## Mobile App
This project will create a login and crud using React and Django Rest Framework and djoser

### Install required dependencies
Type the following command:
`cd frontend; npm install`

### Run on dev environment
Go to your project path and then type the following command:
`npm run start`

### Contribute to the project
Add your changes to the project and then commit and push changes.

Happy coding.