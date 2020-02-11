COMPUTER = 'I am the winner!'
HUMAN = 'You won!'

def ways_to_win(human, computer):
    if human == computer:
        return 'We have a TIE!'

    elif human == 'paper' and computer == 'scissors':
        return COMPUTER

    elif human == 'paper' and computer == 'rock':
        return HUMAN

    elif human == 'scissors' and computer == 'paper':
        return HUMAN

    elif human == 'scissors' and computer == 'rock':
        return COMPUTER

    elif human == 'rock' and computer == 'paper':
        return COMPUTER

    elif human == 'rock' and computer == 'scissors':
        return HUMAN