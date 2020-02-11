from app import app
from app.forms import GameForm
from flask import request, render_template
import random


def ways_to_win(human, computer):
    if human == computer:
        return 'TIE'

    elif human == 'paper' and computer == 'scissors':
        return 'computer is a winner'

    elif human == 'paper' and computer == 'rock':
        return 'human is the winner'

    elif human == 'scissors' and computer == 'paper':
        return 'human is the winner'

    elif human == 'scissors' and computer == 'rock':
        return 'computer is the winner'

    elif human == 'rock' and computer == 'paper':
        return 'computer is the winner'

    elif human == 'rock' and computer == 'scissors':
        return 'human is the winner'

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
