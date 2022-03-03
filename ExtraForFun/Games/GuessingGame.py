import random

list1 = [0,1,2,3,4,5,6,7,8,9]
botChoice = random.choice(list1)
print(botChoice)
guesses = 0
while True:
    ask1 = int(input('Pick A Number 1-10: '))
    if ask1 + botChoice == 10:
        guesses += 1
        print(f'You Win! It only took {guesses} guesses!')
        break
    else:
        print('That\'s Not It! Guess Again!')
        guesses += 1
        continue