from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from cardiacpedia.models import IPG


class Find_Device(FlaskForm):
    manufacturer = StringField('Manufacturer')
    model_number = StringField('Model Number')
    name = StringField('Name')
    submit = SubmitField('Find Device')
