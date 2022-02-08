'''
Created on Mon Feb 7 5:18:20 2022

@author: C. Schulz

Description: Play BlackJack with randomized numbers!

Saved as BlackJack.py
'''

from time import sleep
import random

one = 'One' and 1
two = 'Two' and 2
three = 'Three' and 3
four = 'Four' and 4
five = 'Five' and 5
six = 'Six' and 6
seven = 'Seven' and 7
eight = 'Eight' and 8
nine = 'Nine' and 9
ten = 'Ten' and 10
eleven = 'Eleven' and 11

HowToPlay = 'Ok. Let\'s play! The rules are simple. Try to get your cards to add up to or as close to 21! If you go over, you lose :( Either "Hit" to ask for another card, or "Stay" to not receive anymore cards. If the dealer gets a higher number count than you, without going over 21, they win. Good Luck! '
list1 = [one, two, three, four, five, six, seven, eight, nine, ten, eleven]
card1 = random.choice(list1)
card2 = random.choice(list1)
card3 = random.choice(list1)
card4 = random.choice(list1)
card5 = random.choice(list1)
card6 = random.choice(list1)
card7 = random.choice(list1)
cardDealer1 = random.choice(list1)
cardDealer2 = random.choice(list1)
cardDealer3 = random.choice(list1)

q1 = input('You are going to be playing black jack. Would you like to play? ')
if q1 == 'yes':



    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)



    print(HowToPlay)



    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)



    print('YOUR First Card: ', card1)
    sleep(0.5)
    print('YOUR Second Card: ', card2)
    sleep(0.5)
    print('YOUR Total: ', card1 + card2)



    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)



    print('DEALER\'s First Card: ', cardDealer1)
    print('DEALER\'s Second Card: HIDDEN')



    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)


# Deal Hands
    if card1 + card2 == 21:
        print('CONGRATS! You got 21!')
        quit()
    # Round 1
    else:
        q2 = input('Hit or Stay? ')
        if q2 == 'hit':
            print('YOUR Third Card: ', card3, '. Your new total is', card1 + card2 + card3,'.')
            if card1 + card2 + card3 == 21:
                print('CONGRATS! You got 21! You must stay :)')
            if card1 + card2 + card3 > 21:
                print('Sorry, you busted. You lose :(')
                quit()
        
        if q2 == 'stay':
            print('Ok. Smart decision. Dealer\'s second card being flipped over now...')
            
            
            print('.')
            sleep(0.5)
            print('.')
            sleep(0.5)


            print('DEALER\'S Second Card: ', cardDealer2)
            print('DEALER\'s Total: ', cardDealer1 + cardDealer2)

            if cardDealer1 + cardDealer2 < 17:

                print('Dealer receives cards until they either get 21, go over 21, or get a total of 17+.')
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)
                print('DEALER\'s Third Card: ', cardDealer3)
                sleep(0.5)
                print('DEALER\'s Total: ', cardDealer1 + cardDealer2 + cardDealer3)
                if cardDealer1 + cardDealer2 + cardDealer3 > 21:
                    print('.')
                    sleep(0.5)
                    print('.')
                    sleep(0.5)
                    print('Dealer Busts! You Win! Congrats :)')
                    quit()
                if cardDealer1 + cardDealer2 + cardDealer3 > card1 + card2:
                    print('.')
                    sleep(0.5)
                    print('.')
                    sleep(0.5)

                    print('Dealer Wins! Sorry :(')

                    sleep(0.5)
                    print('------------------')
                    quit()
                if cardDealer1 + cardDealer2 + cardDealer3 < card1 + card2:
                    print('.')
                    sleep(0.5)
                    print('.')
                    sleep(0.5)

                    print('You Win! Congrats :)')
                
                    sleep(0.5)
                    print('------------------')
                    quit()
                if cardDealer1 + cardDealer2 == card1 + card2:
                    print('.')
                    sleep(0.5)
                    print('.')
                    sleep(0.5)

                    print('Push/Tie! :| ')
                
                    sleep(0.5)
                    print('------------------')
                    quit()



            if (cardDealer1 + cardDealer2 > card1 + card2) and (cardDealer1 + cardDealer2) > 17:
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)

                print('Dealer Wins! Sorry :(')

                sleep(0.5)
                print('------------------')
                quit()



            if (cardDealer1 + cardDealer2 < card1 + card2) and (cardDealer1 + cardDealer2) > 17:
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)

                print('You Win! Congrats :)')
                
                sleep(0.5)
                print('------------------')
                quit()



            if (cardDealer1 + cardDealer2 == card1 + card2) and (cardDealer1 + cardDealer2) > 17:
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)

                print('Push/Tie! :| ')
                
                sleep(0.5)
                print('------------------')
                quit()

















        else:
                q3 = input('Hit or Stay? ')
                if q3 == 'hit':
                    print('YOUR FOURTH Card: ', card4, '. Your new total is ', card1 + card2 + card3 + card4)
                    if card1 + card2 + card3 + card4 == 21:
                        print('CONGRATS! You got 21! You must stay :)')
                    if card1 + card2 + card3 + card4 > 21:
                        print('Sorry, you busted. You lose :(')
                        quit()
                    else:
                        q4 = input('Hit or Stay? ')
                        if q4 == 'hit':
                            print('YOUR FOURTH Card: ', card5, '. Your new total is ', card1 + card2 + card3 + card4 + card5)
                            if card1 + card2 + card3 + card4 + card5 == 21:
                                print('CONGRATS! You got 21! You must stay :)')
                            if card1 + card2 + card3 + card4 + card5 > 21:
                                print('Sorry, you busted. You lose :(')
                                quit()
                            else:
                                q5 = input('Hit or Stay? ')
                                if q5 == 'hit':
                                    print('YOUR FOURTH Card: ', card6, '. Your new total is ', card1 + card2 + card3 + card4 + card5 + card6)
                                if card1 + card2 + card3 + card4 + card5 + card6 == 21:
                                    print('CONGRATS! You got 21! You must stay :)')
                                if card1 + card2 + card3 + card4 + card5 + card6 > 21:
                                    print('Sorry, you busted. You lose :(')
                                    quit()
                                else:
                                    q6 = input('Hit or Stay? ')
                                    if q6 == 'hit':
                                        print('YOUR FOURTH Card: ', card6, '. Your new total is ', card1 + card2 + card3 + card4 + card5 + card6 + card7)
                                    if card1 + card2 + card3 + card4 + card5 + card6 + card7 == 21:
                                        print('CONGRATS! You got 21! You must stay :)')
                                    if card1 + card2 + card3 + card4 + card5 + card6 + card7 > 21:
                                        print('Sorry, you busted. You lose :(')
                                        quit()
                    


else:
    print('ok. sorry')
    quit()