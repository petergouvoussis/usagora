from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):

    username = StringField(validators=[InputRequired(), Length(min=3, max=30)], render_kw={'placeholder':'username'})
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=30)], render_kw={'placeholder':'password'})
    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    username = StringField(validators=[InputRequired(), Length(min=3, max=30)], render_kw={'placeholder':'username'})
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=30)], render_kw={'placeholder':'password'})
    submit = SubmitField('Login')
