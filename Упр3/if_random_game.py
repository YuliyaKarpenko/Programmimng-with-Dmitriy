import random
num = random.randint(1,4)
guess1 = int(input('Guess a number between 1 and 4: '))
if guess1 == num:
    print('Yay! You guessed it.')
else: 
    print ('Better luck next time! The answer was ', num)
