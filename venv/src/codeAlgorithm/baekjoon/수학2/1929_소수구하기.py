'''
  문제 : M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

  1) 첫째 줄 - M,N

  해결법
  1) 에라토스테네스의 체 활용
'''

from sys import stdin
from sys import stdout

def find_primenumber(numList, n):
    prime = 2
    limit = int(n**0.5)
    numList[0],numList[1] = False,False

    while prime<=limit:
        if numList[prime]:
            for i in range(prime, n+1):
                if numList[i] and (i%prime==0) and (i!=prime):numList[i]=False
        prime+=1

    return numList

m,n = map(int, stdin.readline().split())
i=0
for n in find_primenumber([True for n in range(n+1)],n):
    if n and i>=m:stdout.write(f'{i}\n')
    i+=1