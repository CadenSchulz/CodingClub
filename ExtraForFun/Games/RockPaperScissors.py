
# Imports
from time import sleep
import random

# Asking If You Want To Play
print(' _________________________________________________')
question1 = input('|Would you like to play "Rock Paper Scissors"? ')
print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

while True:
    # Do You Want To Play?
    if question1.lower() == 'yes':
        print(' ________________')
        print('|Ok. Let\'s play. |')
        print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n')
        print(' _________________________________________')
        print("{} {:8s} {:8s} {:8s}".format('|Choose One: ', '(Rock --', 'Paper --', 'Scissors) |'))
        print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        question2 = input('--> ')
        print('\n')
        if question2.lower() == 'rock':
            print('Ok!')
            sleep(0.25)
            print('3')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('2')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('1')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
        elif question2.lower() == 'paper':
            print('Ok!')
            sleep(0.25)
            print('3')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('2')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('1')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
        elif question2.lower() == 'scissors':
            print('Ok!')
            sleep(0.25)
            print('3')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('2')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('1')
            sleep(0.25)
            print('.')
            sleep(0.25)
            print('.')
            sleep(0.25)
        else:
            print('This is an invalid entry.')
            continue
    
    # List/Bot Picks Their Choice
        list = ['Rock', 'Paper', 'Scissors']
        BotPick = random.choice(list)
        if BotPick == 'Rock':
            print('\t    ______')
            print(f'BOT Chose: | {BotPick} |')
            print('\t    ‾‾‾‾‾‾')
        elif BotPick == 'Paper':
            print('\t    _______')
            print(f'BOT Chose: | {BotPick} |')
            print('\t    ‾‾‾‾‾‾‾')
        elif BotPick == 'Scissors':
            print('\t    __________')
            print(f'BOT Chose: | {BotPick} |')
            print('\t    ‾‾‾‾‾‾‾‾‾‾')

# Display Picks
    # Preview -- Rock Situations
        if (BotPick == 'Rock') and (question2.lower() == 'rock'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Rock       |')
            print(f'| YOUR\'s Pick: Rock      |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if (BotPick == 'Rock') and (question2.lower() == 'paper'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Rock       |')
            print(f'| YOUR\'s Pick: Paper     |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if (BotPick == 'Rock') and (question2.lower() == 'scissors'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Rock       |')
            print(f'| YOUR\'s Pick: Scissors  |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    # Preview -- Paper Situations
        if (BotPick == 'Paper') and (question2.lower() == 'rock'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Paper      |')
            print(f'| YOUR\'s Pick: Rock      |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if (BotPick == 'Paper') and (question2.lower() == 'paper'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Paper      |')
            print(f'| YOUR\'s Pick: Paper     |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if (BotPick == 'Paper') and (question2.lower() == 'scissors'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Paper      |')
            print(f'| YOUR\'s Pick: Scissors  |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    # Preview -- Scissor Situations
        if (BotPick == 'Scissors') and (question2.lower() == 'rock'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Scissors   |')
            print(f'| YOUR\'s Pick: Rock      |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if (BotPick == 'Scissors') and (question2.lower() == 'paper'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Scissors   |')
            print(f'| YOUR\'s Pick: Paper     |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if (BotPick == 'Scissors') and (question2.lower() == 'scissors'):
            print(f' ________________________')
            print(f'| BOT\'s Pick: Scissors   |')
            print(f'| YOUR\'s Pick: Scissors  |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

    # All Rock Situations
        if BotPick == 'Rock' and question2.lower() == 'rock':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} ties YOUR {question2.lower()}  :o          |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        elif BotPick == 'Rock' and question2.lower() == 'paper':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} loses to YOUR {question2.lower()}  :)     |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        elif BotPick == 'Rock' and question2.lower() == 'scissors':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} beats YOUR {question2.lower()}  :(     |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    
    # All Paper Situations
        if BotPick == 'Paper' and question2.lower() == 'rock':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} beats YOUR {question2.lower()}  :(        |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        elif BotPick == 'Paper' and question2.lower() == 'paper':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} ties YOUR {question2.lower()}  :o        |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        elif BotPick == 'Paper' and question2.lower() == 'scissors':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} loses to YOUR {question2.lower()}  :) |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    
    # All Scissors Situations
        if BotPick == 'Scissors' and question2.lower() == 'rock':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} loses to YOUR {question2.lower()}  :)  |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        elif BotPick == 'Scissors' and question2.lower() == 'paper':
            print(f' ____________________________________________')
            print(f'|The BOT\'s {BotPick} beats YOUR {question2.lower()}  :(     |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        elif BotPick == 'Scissors' and question2.lower() == 'scissors':
            print(f' ___________________________________________')
            print(f'|The BOT\'s {BotPick} ties YOUR {question2.lower()}  :o  |')
            print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        
        break

    # Option To Not Play The Game
    else:
        print('Alright! Come again soon :)')
        break