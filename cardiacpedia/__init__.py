import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

##########################################################
##################Flask Config Setup#######################
##########################################################
class ConfigClass(object):
    SECRET_KEY = str(os.urandom(32))
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"

app.config.from_object(__name__+'.ConfigClass')
db = SQLAlchemy(app)
Migrate(app,db)



##########################################################
##################Blueprint configs#######################
##########################################################

from cardiacpedia.core.views import core
from cardiacpedia.error_pages.handlers import error_pages
from cardiacpedia.users.views import users

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
