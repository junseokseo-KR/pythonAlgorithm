'''
    문제)
    자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라
    이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
    예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는
    61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

    입력)
    1) M<=10000 / M<=N
    2) N<=10000

    출력)
    1)M<=소수<=N들의 합과 최솟값
    2)이 사이에 소수가 없을 경우 -1 출력

    다른사람풀이)
    시간 : 76ms

    M = int(input())
    N = int(input())

    check = [False for i in range(N+1)]
    for i in range(2, int(N**0.6)):
        if check[i] == False:
            for j in range(2 * i, N + 1, i):
                check[j] = True
    prime_number = []
    for i in range(M, N + 1):
        if i >= 2:
            if check[i] == False:
                prime_number.append(i)


    if len(prime_number) == 0:
        print(-1)
    else :
        print(sum(prime_number))
        print(min(prime_number))
'''

#나의 풀이 : 612ms
from sys import stdin
from sys import stdout

def is_primenumber(num):
    i = 2
    while (i<=n) and (num%i!=0): i+=1

    if (n>1) and (n==i): return True
    elif (n>1) and (n!=i): return False

m = int(stdin.readline())
n = int(stdin.readline())
sum = 0
min = n

for n in range(m,n+1):
    if is_primenumber(n):
        sum+=n
        if n < min: min=n

if sum==0:
    stdout.write(str(-1))
else:
    stdout.write(f'{sum}\n{min}')