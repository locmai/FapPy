
# FapPy

A two-day pet project using Django Framework to build a Web Application help people to control their masturbation addiction.

A funny idea from my friend and I think it will be helpful to someone.

## Quick Overview
### Features
* Submit M statuses - **Done**
* Sign up, log in, log out - **Done**
* Export data to CSV format - **Done**
* Full analysis support - **Not started due to LAZINESS**
### Stack
I planned to use Django with ReactJS for practicing but then I got lazy and use pure Python with Django.
* Django 2.0.2
* Python 3.6
### Python packages
I used the following packages:
```
pip freeze
Django==2.0.2
django-widget-tweaks==1.4.1
gunicorn==19.7.1
psycopg2==2.7.4
pytz==2018.3
whitenoise==3.3.1
```
## Usage
Simply sign up for new account (demo site below), submit your masturbation reason,method and duration everytime you did. The app will collect the data and help you keep track your status.

## Development
I wrote this app on Window,development is on the branch [Windows stable](https://github.com/locmai/FapPy/tree/win10_stable1.0)  

## Heroku Deployment

The Profile is prepared for Heroku deployment.

### Database configuration:

Edit settings.py in folder *fappy*

## Demo
I'm currently hosting the site on [Heroku](https://fappy.herokuapp.com/).

It might go to sleep after a few minutes for being inactive. 
As a solution, I have used [Pingdom](https://www.pingdom.com) to ping the site every 15 minutes. Hope it will be okay there.

