'''
Created on Wed Mar 9 10:00:34 2022

@author: C. Schulz

Description: Inputting bowling information and outputting scores, average, names, etc.

Saved as prog8f.py
'''

nameFirst = input('Enter Name: ')
nameLast = input('Enter Last Name: ')
nameTeam = input('Enter Team Name: ')
score1 = float(input('FIRST Score: '))
score2 = float(input('SECOND Score: '))
score3 = float(input('THIRD Score: '))
average = 0
num = 0
def AverageScore(average):
    average = (score1 + score2 + score3)/3
    print(f'Average: {average}')
AverageScore(average)

def Display(num):
    print(f'\nPlayer: {nameFirst} {nameLast}\n')
    print(f'Team: {nameTeam}\n')
    print(f'FIRST Game: {score1}')
    print(f'SECOND Game: {score2}')
    print(f'THIRD Game: {score3}\n')
    AverageScore(average)
Display(num)