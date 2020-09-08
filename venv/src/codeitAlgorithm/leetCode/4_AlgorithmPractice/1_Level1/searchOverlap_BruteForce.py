"""
    BruteForce로 구현
    시간 : O(n^2)
"""
def find_same_number(some_list):
    # 코드를 쓰세요
    for i in range(1, len(some_list)):
        re = 0
        for j in range(len(some_list)):
            if i == some_list[j]:
                re += 1
            if re > 1:
                return i


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))