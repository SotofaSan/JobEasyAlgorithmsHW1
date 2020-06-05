# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enter n manually. n > 0


n = int(input('Please enter the number: n > 0 '))

def digits_sum(n):

    length = len(str(n))
    summa = 0

    for i in range(0, length):
        summa += n % 10
        n = n // 10
    return summa

print(f'sum of the digits = {digits_sum(n)}')

