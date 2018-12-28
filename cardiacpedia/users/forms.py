# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from cardiacpedia.models import User


class Add_User_Roles(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired(message='User ID cannot be left blank')])
    role_id = IntegerField('Role ID', validators=[DataRequired(message='Role ID cannot be left blank')])
    submit = SubmitField('Add Role')

class Remove_User_Roles(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired(message='User ID cannot be left blank')])
    role_id = IntegerField('Role ID', validators=[DataRequired(message='Role ID cannot be left blank')])
    submit = SubmitField('Remove Role')

class Add_Roles(FlaskForm):
    role_name = StringField('Role Name', validators=[DataRequired(message='Role name cannot be left blank')])
    submit = SubmitField('Add Role')

class Remove_Roles(FlaskForm):
    role_id = IntegerField('Role ID', validators=[DataRequired(message='Role name cannot be left blank')])
    submit = SubmitField('Remove Role')

class Remove_Users(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired(message='Role name cannot be left blank')])
    submit = SubmitField('Remove Role')
