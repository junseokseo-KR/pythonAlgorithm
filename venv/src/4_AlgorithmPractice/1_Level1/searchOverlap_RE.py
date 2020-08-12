"""
    시간 효율적으로!

    BruteForce로 풀이시 O(n^2)

    풀이 방법
        1) 리스트 정렬후 반복문 돌리기
            -> 어쨋든 O(n^2)
        2) 리스트 반으로 쪼개기
            -> 캐시 사용 재귀??? 어떻게??;
        3) 캐시를 하나 만들어서 존재했던거 표기하기
            -> O(n)
"""


def find_same_number(some_list):
    # 코드를 쓰세요
    cache = {}
    for i in range(len(some_list)):
        if cache.get(some_list[i]) == None:
            cache[some_list[i]] = True
        else:
            return some_list[i]


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))