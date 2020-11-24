from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import InputRequired, ValidationError

from models import User


class LoginForm(FlaskForm):
    username = StringField('username_label', validators=[InputRequired(message="Please fill out this field.")])
    avatar = HiddenField('avatar_label')
    submit = SubmitField('Let\'s Go')

    # Is raised automatically
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username is already in use, please select a different one.")
