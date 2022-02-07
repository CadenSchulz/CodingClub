from time import sleep


print ('Quiz #1')
sleep(0.25)
print('.W.')
sleep(0.25)
print('..E..')
sleep(0.25)
print('...L...')
sleep(0.25)
print('....C....')
sleep(0.25)
print('.....O.....')
sleep(0.25)
print('......M......')
sleep(0.25)
print('.......E.......')
sleep(0.25)
print(' ')
sleep(0.25)
print('.........T.........')
sleep(0.25)
print('..........O..........')
sleep(0.25)
print(' ')
sleep(0.25)
print('............Q............')
sleep(0.25)
print('.............U.............')
sleep(0.25)
print('..............I..............')
sleep(0.25)
print('...............Z...............')
sleep(0.25)
print(' ')
sleep(0.25)
print('.................#.................')
sleep(0.25)
print('..................1..................')
sleep(0.25)
print(' ')
sleep(0.25)
playing = input('Do you want to take the quiz (yes/no)? ')

if playing.lower() == "yes":
    sleep(0.25)
    print("Okay. Sounds good!")
    sleep(0.25)

else:
    sleep(0.5)
    print('Ok.')
    sleep(0.5)
    print('Goodbye.')
    quit()
score = 0


answer = input("- (1 point) What is the first color of the rainbow? ")
if answer.lower() == "red":
    sleep(0.25)
    print('Congrats,', answer.lower(),'is correct!')
    sleep(0.25)
    score += 1
else:
    sleep(0.25)
    print('Sorry,', answer.lower(), 'is incorrect!')
    sleep(0.25)

answer = input("-- (2 points) What is the second color of the rainbow? ")
if answer.lower() == "orange":
    sleep(0.25)
    print('Congrats,', answer.lower(),'is correct!')
    sleep(0.25)
    score += 2
else:
    sleep(0.25)
    print('Sorry,', answer.lower(), 'is incorrect!')
    sleep(0.25)

answer = input("--- (3 points) What is the third color of the rainbow? ")
if answer.lower() == "yellow":
    sleep(0.25)
    print('Congrats,', answer.lower(),'is correct!')
    sleep(0.25)
    score += 3
else:
    sleep(0.25)
    print('Sorry,', answer.lower(), 'is incorrect!')
    sleep(0.25)

answer = input("---- (4 points) What is the fourth color of the rainbow? ")
if answer.lower() == "green":
    sleep(0.25)
    print('Congrats,', answer.lower(),'is correct!')
    sleep(0.25)
    score += 4
else:
    sleep(0.25)
    print('Sorry,', answer.lower(), 'is incorrect!')
    sleep(0.25)

print("Thank you for taking the quiz. You got a " + str(score) + "/10!" + " (" + str((score / 10) * 100) + "%)")