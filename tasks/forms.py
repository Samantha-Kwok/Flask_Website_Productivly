from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField



class TaskForm(FlaskForm):
    item = StringField("Task", validators=[DataRequired(), Length(min=2, max=200)])
    category =StringField("Category (Please choose ONE from Home, Work, Fun, Wellbeing)",validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    submit = SubmitField("Submit")

