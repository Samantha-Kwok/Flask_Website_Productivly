from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed


class PostForm(FlaskForm):
    title=StringField("Title", validators=[DataRequired(), Length(min=2, max=200)])
    subtitle=StringField("Summary",validators=[DataRequired(),Length(min=2, max=100)])
    content=TextAreaField("Content", validators=[DataRequired()])
    submit=SubmitField("Submit")


class UpdatePostForm(FlaskForm):
    title=StringField("Title", validators=[DataRequired(), Length(min=2, max=100)])
    subtitle=StringField("Summary",validators=[DataRequired(),Length(min=2, max=100)])
    content=TextAreaField("Content", validators=[DataRequired()])
    picture = FileField("Upload Your Post Picture", validators=[FileAllowed(["jpg", "png","jpeg"])])
    submit=SubmitField("Update")

 
