from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class ProfileForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    gender = SelectField("Gender", choices=[("male", "Male"), ("female", "Female")], validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=1, max=120)])
    social_class = SelectField("Social Class", choices=[
        ("working_class", "Working Class"),
        ("middle_class", "Middle Class"),
        ("upper_class", "Upper Class")
    ], validators=[DataRequired()])
    country = SelectField("Country", choices=[
        ("poland", "Poland"),
        ("germany", "Germany"),
        ("united_states", "United States"),
        ("uk", "United Kingdom"),
        ("france", "France"),
        ("italy", "Italy"),
        ("spain", "Spain"),
        ("other", "Other")
    ], validators=[DataRequired()])
