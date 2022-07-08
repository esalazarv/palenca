from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
