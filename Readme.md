# Hubspot Integration
# Integration between Hubspot API and Django Admin app
This is a pretty siple django application that allow you to pull the deals from an application created in Hubspot cms.
Authenticacion is handle using OAuth tokens 

# Getting Started
Keep in mind that this application is running under Python 3.9, so we need to install it first.

 - Create Virtual Evn
 - python3.9 -m venv djangoproject
 - cd djangoproject
 - Activate Virtual env
 - source bin/activate
 - mv djangoproject/ source
 - cd source
 - Check database Settings and Hubspot client id and secret
 - pip -r requirements.txt
 - python manage.py migrate
 - python manage.py runserver
 - Enjoy
