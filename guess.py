import random

def guess(x):
    hidden_no = random.randint(1, x)
    guess = 0
    while guess != hidden_no:
        guess = int(input(f'Guess a no between 1 and {x} '))
        if guess < hidden_no:
            print('sorry guess again,too low...')
        elif guess > hidden_no:
            print('sorry guess again,too high...')
        else:
            print(f'Congrats you had guessed the correct no i.e,{hidden_no} :) ')

guess(100)

