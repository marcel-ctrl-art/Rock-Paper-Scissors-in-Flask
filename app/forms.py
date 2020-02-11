from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    choice = SelectField('Your choice', choices=[('scissors', 'scissors'), ('rock', 'rock'), ('paper', 'paper')])
    submit = SubmitField('Submit')