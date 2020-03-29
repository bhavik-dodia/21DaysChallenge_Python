import time
import random

name = input('What is your name? ')
print('\nHello, ' + name + ' time to play Hangman!')
print()
time.sleep(1)

print('Start guessing...')
time.sleep(0.5)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', name]

c = 'y'
while c == 'y':
    word = random.choice(words)
    guesses = ''
    turns = 10
    while turns > 0: 
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('_')
                failed = 1
        
        if failed == 0:
            print('\nCongratulations, You Win!!!')
            print('The word is: ' + word)
            print()
            break
        print()

        guess = input('Guess a character: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('\nOops! wrong guess')
            print('You have ' + str(turns) + ' more guesses.\n')
        
        if turns == 0:
            print('You loose')
    
    c = input('\nDo you want to play again?(y/n) ')