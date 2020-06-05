# Count odd and even numbers.
# Count odd and even digits of the whole number.
# E.g, if entered number 34560,
# then 3 digits will be even (4, 6, and 0)
# and  2 odd digits (3 and 5).

n = int(input('Please enter the number:   '))

even = 0
odd = 0
for x in str(n):
    if int(x) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'{even} even digits and {odd} odd digits')