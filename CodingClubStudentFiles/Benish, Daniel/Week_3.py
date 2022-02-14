count = 0
total = 3
i1 = int(input("What is 1+44? "))
if(i1 == 45):
    print("Correct!")
    count+=1
else:
    print("Incorrect!")
 
i2 = int(input("What is 12*12? "))
if(i2 == 144):
    print("Correct!")
    count+=1
else:
    print("Incorrect!")
 
i3 = int(input("What is 100*2? ") )
if(i3 == 200):
    print("Correct!")
    count+=1
else:
    print("Incorrect!")
 
print("\nTotal Correct: ", count, " out of ", total)
print("Percentage: ", (count/total) * 100, "%")

'''
W
'''