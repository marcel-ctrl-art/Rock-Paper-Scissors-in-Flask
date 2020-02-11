from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    choice = SelectField('Please pick your tool:', choices=[('scissors', 'scissors'), ('rock', 'rock'), ('paper', 'paper')])
    submit = SubmitField('Submit')