listik = ['leg', 'gang', 'stand']
import random
s = random.choice(listik)
r = random.choice(s)
for i in s:
    if i == r:
        print ('?')
    else:
        print(i)
g = input ('Guess the missing letter')
if g == r:
    print ('Good job! The word was:',s)
else: 
    print ('Better luck next time!The word was:',s)
