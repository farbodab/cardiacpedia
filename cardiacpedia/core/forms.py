from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from wtforms import ValidationError

class Contact(FlaskForm):
    fname = StringField('First Name *', validators=[DataRequired(message='Please enter your first name')])
    lname = StringField('Last Name *', validators=[DataRequired(message='Please enter your last name')])
    email = StringField('Email *', validators=[DataRequired(message='Please enter your email'), Email(message='Please enter a valid email')])
    comment = TextField('Please enter your comments here *', validators=[DataRequired('This field cannot be left blank')])
    submit = SubmitField('Send Message')
