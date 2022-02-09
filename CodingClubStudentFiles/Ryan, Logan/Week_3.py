print("Quiz 1")
 
n = 0
for i in list("WELCOME TO QUIZ #1"):
    if i != " ":
        print("."*n,i,"."*n)
    else:
        print("")
    n+=1
 
Questions = """Do you want to take the quiz? (yes/no): [0:yes
- (1 point) what is the first color of the rainbow: [1:red
-- (2 points) what is the second color of the rainbow: [2:orange
--- (3 points) what is the third color of the rainbow: [3:yellow
---- (4 points) what is the fourth color of the rainbow: [4:green"""
 
userTotal = 0
amountTotal = 0
 
for i in Questions.split("\n"):
    
    question = i.split("[")[0]
    
    points = int(i.split("[")[1].split(":")[0])
    answer = i.split("[")[1].split(":")[1]
    
    userAnswer = input(question).capitalize()
    
    if userAnswer == answer.capitalize():
        print("Congrats, {} is correct! (+{})".format(userAnswer, points))
        userTotal += points
    else:
        print("Sorry, {} is incorrect".format(userAnswer))
    amountTotal += points
 
print("Thank you for taking this quiz. You got a {}/{} ({}%)".format(userTotal,amountTotal, (userTotal/amountTotal*100)))



# What To Fix: 

'''You could make it so that after you ask the question 
“Want to take the quiz? (yes/no)”, if I say “no”, you 
say “ok goodbye” and then use a quit() import function 
to end the program.
'''


'''
Also, you could make it so that the code uses a “sleep import”, 
which makes a delay in how fast the lines in the output show up. 
This just makes a cleaner look and more appealing to the viewer. 
You can do this by typing “from time import sleep” at the top of 
your code, then inside the code, type “sleep(1)”. This will make 
it delay by one second. If you want to delay it by 2 seconds, it 
would be “sleep(2)”. You get the point.
'''