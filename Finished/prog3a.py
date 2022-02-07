'''
Created on Mon Feb 1 10:21:34 2022
@author: C. Schulz
Description: Employee hours and pay rate inputted.
Saved as prog3a.py
'''

from time import sleep


print('.')                        # For cleaner formatting
sleep(0.25)                       # For cleaner formatting
print('.')                        # For cleaner formatting
sleep(0.25)                       # For cleaner formatting
print('.')                        # For cleaner formatting
sleep(0.25)                       # For cleaner formatting


name = input('Your Name (First, Last): ')
employeeNumber = input('Your Employee ID Number: ')
hours = float(input('Hours Worked: '))
rate = float(input('Pay Rate ($): '))
grossPay = hours * rate
taxRate = 0.1173
taxes = grossPay * taxRate
netPay = grossPay - taxes

                                                      #  ___________________________________________________
print('.')                                            # | This is just to make the formatting look cleaner. |
sleep(0.25)                                           # |                                                   |
print('.')                                            # |                      o     o                      |
sleep(0.25)                                           # |                    |_________|                    |
print('-----------------------')                      # |                                                   |
sleep(0.25)                                           # | This is just to make the formatting look cleaner. |
                                                      # |___________________________________________________|

print('Caden\'s Clothing Store')



print('') # For cleaner formatting



print(name)
print(employeeNumber)



print('') # For cleaner formatting



print("{} {:10s} {:10s} {:10s} {:10s}".format('Hours', 'Rate'.center(15), 'Gross Pay'.center(15), 'Taxes'.center(15), 'Net Pay'.center(15)))
print("{:2.0f} {:14.2f} {:14.2f} {:15.2f} {:15.2f}".format(hours, rate, float(grossPay), float(taxes), float(netPay)))



print('-----------------------')  # For cleaner formatting
sleep(0.25)                       # For cleaner formatting
print('.')                        # For cleaner formatting
sleep(0.25)                       # For cleaner formatting
print('.')                        # For cleaner formatting
sleep(0.25)                       # For cleaner formatting