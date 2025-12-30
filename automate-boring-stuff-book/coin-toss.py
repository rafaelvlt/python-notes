import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname) s- %(message)s')
logging nao deve aparecer para o usuario

#sets the guess to be a string and checks if the user inputed a valid guess
guess = ""
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Guess is ' + guess)
#toss the coin and checks the user guess, i added the if and else part bcs the original code didn't have
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1:
    toss = 'heads'
else:
    toss = 'tails'
logging.debug('Toss is: ' + str(toss))
#checks the toss against the guess
if toss == guess:
    print('You got it!')
#else, you have another try to guess the same coin.
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
