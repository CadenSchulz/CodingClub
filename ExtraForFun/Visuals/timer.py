from time import sleep


ask = int(input('Minutes: '))
sleep(0.5)
ask2 = int(input('Seconds: '))

minutes = ask * 60
seconds = ask2

sleep(1)
print(f'\nTimer Started...')
print(f'-----')
print(f'{ask}:{ask2}')
sleep(minutes)
sleep(seconds)
print('\n')
print(f' ___________________')
print(f'|{ask}:{ask2} Timer Finished |')
print(f' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
quit()