import utils
import random
player_name = input('Enter your name: ')
print('\nGood Luck, ' + player_name + '...')
c= 'y'
while c == 'y':
    print('\nPick a hand: (0: Rock, 1: Paper, 2: Scissors)')
    player_hand = int(input('Enter your choice (0-2): '))
    if utils.validate(player_hand):
        computer_hand = random.randint(0, 2) 
        print()
        utils.print_hand(player_hand, player_name)
        utils.print_hand(computer_hand, 'Computer')
        result = utils.judge(player_hand, computer_hand)
        print('\nResult: ' + result)
    else:
        print('\nPlease enter a valid number!!!')
        continue
    c = input('\nDo you want to play again?(y/n) ')