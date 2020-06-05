# Find max number from 3 values, entered manually from a keyboard

max3 = int(input('Please enter the first number:   '))
n2 = int(input('Please enter the second number:   '))
n3 = int(input('Please enter the third number:   '))

if max3 < n2:
        max3 = n2
if max3 < n3:
        max3 = n3

print(f'max number from 3 values = {max3}')
