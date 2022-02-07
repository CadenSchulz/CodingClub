'''
Created on Mon Feb 2 10:54:32 2022
@author: C. Schulz
Description: Computing commission of a salesperson
Saved as prog4a.py
'''


from time import sleep


sale = float(input('Montly Sales ($): '))
commission = float(sale * 0.2)



print('.')              #For Cleaner Formatting
sleep(0.5)              #For Cleaner Formatting
print('.')              #For Cleaner Formatting
sleep(0.5)              #For Cleaner Formatting
print('____________')   #For Cleaner Formatting
sleep(0.5)              #For Cleaner Formatting



print("{} {:.2f}".format('Monthly Sales ($): ', float(sale)))
sleep(0.5) #For Cleaner Formatting
print("{} {:.2f}".format('Commission Earned ($): ', float(commission)))

print('____________')   #For Cleaner Formatting
sleep(0.5)              #For Cleaner Formatting
print('.')              #For Cleaner Formatting
sleep(0.5)              #For Cleaner Formatting
print('.')              #For Cleaner Formatting
sleep(0.5)              #For Cleaner Formatting