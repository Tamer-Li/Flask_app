from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, \
    FileField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')


class PageForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('Save')


class UploadFileForm(FlaskForm):
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField('Upload')


class EditPermissionsForm(FlaskForm):
    admin = StringField('Admin')
    editor = StringField('Editor')
    reared = StringField('Reader')
    bot = StringField('Bot')
    submit = SubmitField('Save')
