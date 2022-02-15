score=0
ans1=input('What is 2+2? ')
if ans1 =='4':
    print('Correct!')
    score=score+1
    print(score)
else:
    print('The correct answer was 4. Continue')
ans2=input('What is 3+3? ')
if ans2== '6':
    print('Correct!')
    score=score+1
    print(score)
else:
    print('The correct answer was 6.')
print()
print()
print(f"{'Your score was a:'}{(score/2)*100:.2f}")