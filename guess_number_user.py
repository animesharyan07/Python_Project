import random

def guess_number(x):
    random_number=random.randint(1,x)
    guess=0

    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}:-'))
        if(guess< random_number):
            print('Sorry ! you guessed too low')
        elif guess>random_number:
            print('Sorry ! you guessed too high')

    print(f"Congratulations you have guessed the right number that is  {random_number}")

guess_number(15)