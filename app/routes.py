from app import app
from app.forms import GameForm
from flask import request, render_template


@app.route('/')
def index():
    form = GameForm()
    return render_template('index.html', form=form)


@app.route('/winner', methods=['GET', 'POST'])
def winner(choice=None):
    human = request.form['choice']

    CHOICES = ('paper', 'scissors', 'rock')
    computer = random.choice(CHOICES)

    winner = ways_to_win(request.form['choice'], computer)

    return render_template(
        'winner.html',
        human=human,
        computer=computer,
        winner=winner

    )
