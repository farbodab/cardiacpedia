import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from flask_bootstrap import Bootstrap
from config import Config

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
