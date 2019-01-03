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

class Finder(FlaskForm):
    type = SelectField('Device Type', choices=[('IPG','IPG Low-Voltage Devices'),
    ('CRTP','CRT-P Low-Voltage Devices'),('ICD','ICD High-Voltage Devices'),
    ('CRTD','CRT-D High-Voltage Devices'),('LV','LV Low-Voltage Devices'),
    ('HV','HV High-Voltage Devices')],validators=[DataRequired(message='You must select a device type')])
    manufacturer = StringField('Manufacturer')
    model_number = StringField('Model Number')
    name = StringField('Name')
    submit = SubmitField('Find Device')
