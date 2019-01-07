import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(os.urandom(32))
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:Kalimdor1996@localhost:3306/cardiacbook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'mbox.freehostia.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'farbod@deepmedsolutions.com'
    MAIL_PASSWORD = 'kalimdor1996'
    MAIL_DEFAULT_SENDER = '"CardiacPedia" <noreply@cardiacpedia.com>'
    #hello

    # Flask-User settings
    USER_APP_NAME = "CardiacPedia"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@cardiacpedia.com"
