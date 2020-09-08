import time

start = time.time()
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        pic = 0

        while pic != len(s):
            if s[pic] in ['I', 'X', 'C']:
                if s[pic:pic + 2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                    res += (dic.get(s[pic + 1]) - dic.get(s[pic]))
                    pic += 2
                else:
                    res += dic.get(s[pic])
                    pic += 1
            else:
                res += dic.get(s[pic])
                pic += 1

print("실행시간 : ",time.time()-start)