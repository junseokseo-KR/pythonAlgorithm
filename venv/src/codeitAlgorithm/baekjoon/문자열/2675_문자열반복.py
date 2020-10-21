import sys
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

cnt = int(input())

for _ in range(cnt):
    res = ""
    val = sys.stdin.readline().rstrip().split(' ')
    for s in val[1]:
        if s in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:":
            res += int(val[0])*s
    print(res)

#
# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i
#     print(text)