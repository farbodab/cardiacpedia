from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from cardiacpedia.models import IPG

class Device_Type(FlaskForm):
    type = SelectField('Device Type', choices=[('IPG','IPG Low-Voltage Devices'),
    ('CRTP','CRT-P Low-Voltage Devices'),('ICD','ICD High-Voltage Devices'),
    ('CRTD','CRT-D High-Voltage Devices'),('LV','LV Low-Voltage Devices'),
    ('HV','HV High-Voltage Devices')])

class Device_New(FlaskForm):
    paced = SelectField('Chambers Paced', choices=[("", "---"), ('D','Dual (A+V)'),
    ('A','Atrium'),('V','Ventricle')])

    sensed = SelectField('Chambers Sensed', choices=[("", "---"),('D','Dual (A+V)'),
    ('A','Atrium'),('V','Ventricle')])
    submit = SubmitField('Find Device')

    manufacturer = StringField('Manufacturer')

class Devices_Change(FlaskForm):

    paced = SelectField('Chambers Paced', choices=[("", "---"), ('D','Dual (A+V)'),
    ('A','Atrium'),('V','Ventricle')])

    sensed = SelectField('Chambers Sensed', choices=[("", "---"),('D','Dual (A+V)'),
    ('A','Atrium'),('V','Ventricle')])
    submit = SubmitField('Find Device')

    ra = SelectField('RA Connector', choices=[("", "---"),("3.2 mm C","3.2 mm C"), ("3.2 mm LP","3.2 mm LP"), ("4.75 mm", "4.75 mm"),
    ("4.75 mm Bif Bi.", "4.75 mm Bif Bi."), ("5 mm Uni", "5 mm Uni"), ("5 mm", "5 mm"), ("5 mm Bif", "5 mm Bif"), ("5/6 mm Uni", "5/6 mm Uni"),
    ("6 B", "6 B"), ("6 L", "6 L"), ("6 L-I", "6 L-I"), ("6.1 mm","6.1 mm"), ("6.5 mm", "6.5 mm"), ("Bayonet", "Bayonet"), ("CKP","CKP"),
    ("CPI","CPI"), ("DF-1", "DF-1"), ("DF-1 (1 port)", "DF-1 (1 port)"), ("DF-1 (2 ports)", "DF-1 (2 ports)"), ("DF-1 (3 ports)", "DF-1 (3 ports)"),
    ("DF4","DF4"),("ELA","ELA"),("HV-1", "HV-1"), ("IS-1 BI", "IS-1 BI"), ("IS-1 UNI","IS-1 UNI"), ("Linear", "Linear"), ("LV-1", "LV-1"),
    ("PSI","PSI"), ("SOR", "SOR"), ("Spring clip", "Spring clip"), ("Thermistor", "Thermistor"), ("Vitatron", "Vitatron"), ("VS-1", "VS-1"),
    ("VS-1A","VS-1A"), ("VS-1B", "VS-1B")])

    rv = SelectField('RV Connector', choices=[("", "---"),("3.2 mm C","3.2 mm C"), ("3.2 mm LP","3.2 mm LP"), ("4.75 mm", "4.75 mm"),
    ("4.75 mm Bif Bi.", "4.75 mm Bif Bi."), ("5 mm Uni", "5 mm Uni"), ("5 mm", "5 mm"), ("5 mm Bif", "5 mm Bif"), ("5/6 mm Uni", "5/6 mm Uni"),
    ("6 B", "6 B"), ("6 L", "6 L"), ("6 L-I", "6 L-I"), ("6.1 mm","6.1 mm"), ("6.5 mm", "6.5 mm"), ("Bayonet", "Bayonet"), ("CKP","CKP"),
    ("CPI","CPI"), ("DF-1", "DF-1"), ("DF-1 (1 port)", "DF-1 (1 port)"), ("DF-1 (2 ports)", "DF-1 (2 ports)"), ("DF-1 (3 ports)", "DF-1 (3 ports)"),
    ("DF4","DF4"),("ELA","ELA"),("HV-1", "HV-1"), ("IS-1 BI", "IS-1 BI"), ("IS-1 UNI","IS-1 UNI"), ("Linear", "Linear"), ("LV-1", "LV-1"),
    ("PSI","PSI"), ("SOR", "SOR"), ("Spring clip", "Spring clip"), ("Thermistor", "Thermistor"), ("Vitatron", "Vitatron"), ("VS-1", "VS-1"),
    ("VS-1A","VS-1A"), ("VS-1B", "VS-1B")])

    manufacturer = StringField('Manufacturer')

class Device_Find(FlaskForm):
    manufacturer = StringField('Manufacturer')
    model_number = StringField('Model Number')
    name = StringField('Name')
    submit = SubmitField('Find Device')
