# Django Tutorial
Django is python based framework tha tis used to create webservers.
It is modular so one can remove parts of it.

Elements of Django:
+ Template engine;
+ Object relation map -> allows the user to manipulate a python class and use database;
+ Routing -> Takes in an url and activates a callable python function)
+ Views -> business logic -> always accept a request and return a response or exception.

# startproject details:
+ The outer mysite/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

+ manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

+ The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

+ mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

+ mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

+ mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

+ mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.