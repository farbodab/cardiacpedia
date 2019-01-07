# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from flask_login import current_user
from cardiacpedia.models import User


class Add_User_Roles(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired(message='User ID cannot be left blank')])
    role_id = StringField('Role Number', validators=[DataRequired(message='Role ID cannot be left blank')])
    submit = SubmitField('Add Role')

class Remove_Users(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired(message='Role name cannot be left blank')])
    submit = SubmitField('Remove User')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email cannot be left blank'), Email(message='Please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired(message='Password cannot be left blank')])
    submit = SubmitField('Log In')

class EmailForm(FlaskForm):
    email = StringField('New email', validators=[DataRequired(message='Email cannot be left blank'), Email(message='Please enter a valid email address')])
    password = PasswordField('Current password', validators=[DataRequired(message='Password cannot be left blank')])
    submit = SubmitField('Save')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
    def check_password(self,field):
        if not current_user.check_password(field.data):
            raise ValidationError('The entered password did not match our records!')

def check_password(form,field):
    if not current_user.check_password(field.data):
        raise ValidationError('The entered password did not match our records!')


class PasswordForm(FlaskForm):
    curr_password = PasswordField('Current password', validators=[check_password, DataRequired(message='Current password cannot be left blank'), Length(min=6, max=30, message='Password must be longer than 6 characters')])
    new_password = PasswordField('New password', validators=[DataRequired(message='New password cannot be left blank'),EqualTo('confirm_password', message='Passwords Must Match!'), Length(min=6, max=30, message='Password must be longer than 6 characters')])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(message='Confirm new password cannot be left blank'), EqualTo('new_password', message='Passwords Must Match!')])
    submit = SubmitField('Save')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email cannot be left blank'),Email(message='Please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired(message='Password cannot be left blank'), Length(min=6, max=30, message='Password must be longer than 6 characters')])
    submit = SubmitField('Continue')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
