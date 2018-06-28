import time
import random
from random import randint

### HAGNMAN ###

letters = []

# Print a header title
print('\n\n[-Hangman : by harndt : type help-]')
print('\n\n\n------------------------')
print('        HANGMAN')
print('------------------------')

# Start application
def start():
    print('\n----------')
    print('\n[-MAIN MENU-]')
    print('\n1.) play - sort a word')
    print('2.) quit - end game')

    cmdlist = ['1','2',]
    cmd = getcmd(cmdlist)

    # When command is 1 iniciate variables
    if cmd == '1':
        letters = sort_word()
        limbs = 0
        choices = []
        
        print('\n----------')
        print('\nHere is you re word\n')
        # Print '_' for each position in the word
        for letter in letters:
            print('_ ', end="")
        print('\n----------')
		
        # Run while there are limbs to hang
        while limbs < 3:			
            # Receive a guess to the word
            guess = input('\n>Say your guess: ')
            
            # Input guesses in a separete list
            choices.append(guess)
            
            # Victory variable <<< doesn't work >>>
            victory = 0
            
            # When a guess don't belong it our word add 1 to the total
            # of limbs hanged
            if guess not in letters:
                limbs += 1
            
            # While victory differs from letter size print each char in letters
            if victory != len(letters):
                print('\n' * 100)
                for letter in letters:
                    if letter in set(letters).intersection(choices):
                        print(letter + ' ', end="")
                    else:
                        print('_ ', end="")
    
                # hang a limb from our player
                print('\nYou lose %d of 3 limbs.' % limbs)
            # When victory is the same size as letter show victory message
            # But we'll never enter here apparently ):
            else:
                print('\n' * 100)
                print("    VICTORY    \n")
                print(" _________     \n")
                print("|         |    \n")
                print("|              \n")
                print("|              \n")
                print("|         0    \n")
                print("|        /|\   \n")
                print("|        / \   \n")
                
        # Print game over message whem all your three limbs are hanged
        print('\n' * 100)
        print("   GAME OVER   \n")
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|        /|\   \n")
        print("|        / \   \n")
        print("|              \n")
        print("|              \n")
        
        time.sleep(2)
        start()

    # end application
    elif cmd == '2':
        print('You run away from the gallows')
        time.sleep(1)
        print('For now...')

def sort_word():
    word = randint(0,9)
    if word == 0:
        letters = ['s','i','n','g','e','r']
    elif word == 1:
        letters = ['d','e','v','i','a','t','i','o','n']
    elif word == 2:
        letters = ['s','t','i','c','k']
    elif word == 3:
        letters = ['o','b','s','t','a','c','l','e']
    elif word == 4:
        letters = ['c','a','l','c','u','l','a','t','i','o','n']
    elif word == 5:
        letters = ['r','e','v','i','v','a','l']
    elif word == 6:
        letters = ['v','e','r','d','i','c','t']
    elif word == 7:
        letters = ['p','o','u','n','d']
    elif word == 8:
        letters = ['s','a','t','i','s','f','i','e','d']
    elif word == 9:
        letters = ['a','i','r']
    return letters

# get input from our user
def getcmd(cmdlist):
    cmd = input('\nInput:> ')
    if cmd in cmdlist:
        return cmd
    elif cmd == 'help':
        print('\nType quit to suicide')
        return getcmd(cmdlist)
    elif cmd == 'quit':
        print('\n----------')
        time.sleep(1)
        print('\nSuddely its hard to breathe')
        time.sleep(1)
        print('A last breath runs through  your body')
        time.sleep(1)
        print('Without control your body struggles in vain in the air')
        time.sleep(1)
        print('Until it stops')
        exit(0)
    else:
        print('\n   error. invalid command-\n')
        return getcmd(cmdlist)

if __name__ == "__main__":
    start()
