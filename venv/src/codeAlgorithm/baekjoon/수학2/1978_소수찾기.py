'''
    1) N<=100
    2) 1000 이하의 자연수 N개
'''
from sys import stdin
from sys import stdout

def find_primenumber(numList):
    cnt = 0

    for n in numList:
        i = 2
        while (i<=n) and (n%i!=0):
            i+=1
        if n==i:
            cnt+=1

    return cnt

n = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))
stdout.write(f'{find_primenumber(numList)}')