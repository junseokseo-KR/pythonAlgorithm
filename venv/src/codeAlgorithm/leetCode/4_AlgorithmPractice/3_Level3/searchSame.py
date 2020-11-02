def find_same_number(some_list, start=0, end=None):
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    # 코드를 쓰세요
    if end is None:
        end = len(some_list) - 1
    if start == end:
        return None

    for i in range(start + 1, len(some_list)):
        if some_list[start] == some_list[i]:
            return some_list[start]

    
    start += 1
    return find_same_number(some_list, start)


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

"""
    시간복잡도 : O(n)???
    공간복잡도 : O(n)지만
    리스트를 반으로 나누는 방법으로도 구현해보자
"""