import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

##########################################################
##################CONFIGURATIONS##########################
##########################################################

app.config['SECRET_KEY'] = '\x0c\xf7\x91\xab\xd0\x12\x90\xb7\x7fp\x18rqh\xefF'


##########################################################
##################DATABASE SETUPS#########################
##########################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##########################################################
##################LOGIN CONFIGS#########################
##########################################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

##########################################################
##################Blueprint configs#######################
##########################################################

from cardiacpedia.core.views import core
from cardiacpedia.error_pages.handlers import error_pages
from cardiacpedia.users.view import users

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
