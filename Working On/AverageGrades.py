q1 = input('Do You Want To Calculate Your Average? ')
if q1 == 'yes':
    def Average(y):
        total = 0
        for x in range(1,z):
            grade = int(input('Grade: '))
            total += grade
        average = total/y
        print(f'Average: {average}')

    y = int(input('How many classes do you have? '))
    z = y + 1
    Average(y)

    q2 = input('Would You Like To Start Over? ')
    if q2 == 'yes':
        Average(y)
    else:
        print('Thank You! Good Bye!')
else:
    print('Ok. Bye!')