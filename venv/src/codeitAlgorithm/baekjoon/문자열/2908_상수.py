import sys
a,b = map(str, sys.stdin.readline().rstrip().split())

a = int(a[::-1])
b = int(b[::-1])

print(a if a>b else b)
