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


# 합병 정렬
def merge_sort(my_list):
    _len = len(my_list)
    if _len != 1:
        return merge(merge_sort(my_list[:int(_len / 2)]),merge_sort(my_list[int(_len / 2):]))
    else:
        return my_list

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))