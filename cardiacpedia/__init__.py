import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


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

app.register_blueprint(core)
