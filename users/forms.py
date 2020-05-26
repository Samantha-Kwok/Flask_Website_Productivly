from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, PasswordField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from todolist.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField ("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired() ])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError("That username is taken. Please choose a differnet one.")


    def validate_email (self,email):
        user= User.query.filter_by(email=email.data).first()
        if user :
            raise ValidationError("That email is taken. Please choose a differnet one.")
    

class LoginForm(FlaskForm):
    email = StringField ("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
 
class UpdateAccountForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField ("Email", validators=[DataRequired(), Email()])
    picture= FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    def validate_username(self,username):
        if username.data != current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is taken. Please choose a differnet one.")


    def validate_email (self,email):
        if email.data != current_user.email:
            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken. Please choose a differnet one.")



class RequestResetForm(FlaskForm):
    email = StringField ("Email", validators=[DataRequired(), Email()])
    submit = SubmitField(" Request Password Reset")
    
    def validate_email (self,email):
        user= User.query.filter_by(email=email.data).first()
        if user is None :
            raise ValidationError("That is no accoutn with taht email. You must reigster first.")



class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired() ])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")
