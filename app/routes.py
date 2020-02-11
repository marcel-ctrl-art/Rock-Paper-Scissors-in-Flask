from app import app
from app.forms import GameForm
from flask import request, render_template


@app.route('/')
def index():
    form = GameForm()
    return render_template('index.html', form=form)
