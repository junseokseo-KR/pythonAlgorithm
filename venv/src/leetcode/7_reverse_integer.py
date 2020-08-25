import math


class Solution:
    def reverse(self, x: int) -> int:
        intList = []
        res = 0
        cnt = 0
        sign = 1

        # x가 0보다 작으면 sign 변수에 음수 저장후 x 양수 전환
        if x < 0:
            sign *= -1
            x *= -1

        while x >= 10:
            intList.append(x % 10)
            x //= 10
            cnt += 1

        intList.append(x % 10)

        for i in intList:
            res += i * (10 ** cnt)
            cnt -= 1

        if sign < 0:
            res *= sign

        # integer의 범위를 넘어서면 0 리턴
        if res >= math.pow(2, 31) - 1 or res <= -(math.pow(2, 31)):
            return 0
        else:
            return res