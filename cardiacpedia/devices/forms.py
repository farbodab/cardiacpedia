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

class Devices(FlaskForm):
    type = SelectField('Device Type', choices=[('IPG','IPG Low-Voltage Devices')])

    # type = SelectField('Device Type', choices=[('IPG','IPG Low-Voltage Devices'),
    # ('CRTP','CRT-P Low-Voltage Devices'),('ICD','ICD High-Voltage Devices'),
    # ('CRTD','CRT-D High-Voltage Devices'),('LV','LV Low-Voltage Devices'),
    # ('HV','HV High-Voltage Devices')],validators=[DataRequired(message='You must select a device type')])

    paced = SelectField('Chambers Paced', choices=[('D','Dual (A+V)'),
    ('A','Atrium'),('V','Ventricle')],validators=[DataRequired(message='You must select a pacing configuration')])

    sensed = SelectField('Chambers Sensed', choices=[('D','Dual (A+V)'),
    ('A','Atrium'),('V','Ventricle')],validators=[DataRequired(message='You must select a sensing type')])
    submit = SubmitField('Find Device')

    # ra = SelectField('RA Connector', choices=[('D','3.2 mm C'),
    # ('A','3.2 mm LP Bi.'),('V','3.2 mm LP#'),('V','3.2/5 mm'),
    # ('V','4.75 mm Bif Bi.'),('V','5 mm Bif'),('V','5 mm'),('V','5 mm/Thermistor')
    # ('V','6 mm C'),('V','6 mm B'),('V','6 mm L-I'),('V','A-Track™')
    # ('V','A-V Data™'),('V','3.2 mm LP#'),('V','3.2 mm LP#'),('V','3.2 mm LP#')
    # ('V','3.2 mm LP#'),('V','3.2 mm LP#')],validators=[DataRequired(message='You must select a sensing type')])
    #
    # rv = SelectField('RV Connector', choices=[('D','Dual (A+V)'),
    # ('A','Atrium'),('V','Ventricle')],validators=[DataRequired(message='You must select a sensing type')])

    manufacturer = StringField('Manufacturer')
