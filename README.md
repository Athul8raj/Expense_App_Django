# An Expense app with Django2.0 and pipenv with Social media logins

## Hosted at https://athulraj.pythonanywhere.com

This is a simple and basic expense app where users can register, login, view, and manipulate their expenses.
This website is powered by Django 2.0 and its dependencies

## For local use.

Download the files and folders within this branch and do the following:
1. Do a **pip install pipenv** in your terminal (pip3, python3.6 is preferred)
   Pipenv is a environment-wrapper as well as a package manager.It will enable to handle the virtual environment as well as libraries.For more details on pipenv please visit [here](https://pipenv.readthedocs.io/en/latest/)

2. Once you have pipenv,it is very easy,just run **pipenv run shell** to activate the virtual env

3. Run **pipenv install** where the pipfile and pipfile.lock are present(Do not change anything inside these files as the dependencies are marked in hashes

4. On the folder where manage.py resides, run **python manage.py runserver**. Make sure DEBUG is set to True in settings.py if not already

5.Go to 127.0.0.1:8000/ to view the website.You can register,login using social media including Github,twitter,facebook.You should make application in respective social media sites and add the id and key from the applications into settings.py file.You can add you own social media backend OAuths by adding neceesary statements in setting.py file(AUTHENTICATION_BACKENDS)

## About the Django App

This app uses Django 2.0 version with all of its pre-built dependencies. Django-filter,social-django,crispy tags are some of the external dependencies added.The app is tested using Coverage. The login ,registering and other user authentication stuff is handled by the "users" app inside this app.This app make use of the in-memory sqllite database, although you can configure any other relational databases like Postgres,MySQL, or use DaaS like ElephantSQl etc.

## About pythonanywhere.com
This is a python app hosting website where you can deploy your apps based on Flask,Django,Bottle etc.For more details visit [here](https://pythonanywhere.com)