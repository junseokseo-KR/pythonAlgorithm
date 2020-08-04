def merge(list1, list2):
    resList = []
    len1 = len(list1)
    len2 = len(list2)
    # 코드를 작성하세요.
    for i in range(len1 + len2):
        if len1 != 0 and len2 == 0:
            resList.append(list1[0])
            del list1[0]
        elif len1 == 0 and len2 != 0:
            resList.append(list2[0])
            del list2[0]
        else:
            if list1[0] > list2[0]:
                resList.append(list2[0])
                del list2[0]
                len2 = len(list2)
            else:
                resList.append(list1[0])
                del list1[0]
                len1 = len(list1)
    return resList


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))