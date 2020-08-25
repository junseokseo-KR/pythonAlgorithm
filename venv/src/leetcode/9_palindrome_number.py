"""
str 사용버전
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        return x==int(str(x)[::-1])
"""
class Solution:
    def reverseInteger(self, x: int) -> int:
        intList = []
        cnt = 0

        while x >= 10:
            intList.append(x % 10)
            x //= 10
            cnt += 1

        intList.append(x % 10)
        x = 0

        for i in intList:
            x += i * (10 ** cnt)
            cnt -= 1

        return x

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        res = self.reverseInteger(x)

        if res == x:
            return True
        else:
            return False