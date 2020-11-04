from sys import stdin
from sys import stdout

def get_digit(n):
    digit = list()
    while n>=10:
        digit.append(n%10)
        n//=10
    digit.append(n)
    return digit

def find_divide_sum(min, max):
    for n in range(min, max):
        digit=get_digit(n)
        digit.append(n)
        if sum(digit)==max:
            return n
    return 0

max = int(stdin.readline())
digit = get_digit(max)
min = max-(9*len(digit))

stdout.write(f'{find_divide_sum(min,max)}\n')