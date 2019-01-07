import os
from flask import Flask
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import stripe
from functools import wraps


def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_anonymous:
                return redirect(url_for('users.login'))
            if not current_user.allowed(access_level):
                return redirect(url_for('core.index', message="You do not have access to that page. Sorry!"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(os.path.sep, basedir, 'templates','flask_user')

##########################################################
##################Flask Config Setup#######################
##########################################################


db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"



##########################################################
##################Blueprint configs#######################
##########################################################

from cardiacpedia.core.views import core
from cardiacpedia.error_pages.handlers import error_pages
from cardiacpedia.users.views import users
from cardiacpedia.devices.views import devices

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(devices)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('CardiacBook startup')
