# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    big = start
    i = start
    while i != end:
        if my_list[end] >= my_list[i]:
            swap_elements(my_list, i, big)
            i += 1
            big += 1
        else:
            i += 1
    swap_elements(my_list, i, big)
    return big


# 퀵 정렬
def quicksort(my_list, start=None, end=None):
    _len = len(my_list)
    mid = int(_len / 2)
    if start==None:
        start=0
    if end==None:
        end=_len-1


    # base case : 리스트의 크기가 가장 작을때
    if end-start < 1:
        return
    pivot = partition(my_list,start,end)

    quicksort(my_list,start,pivot-1)

    quicksort(my_list,pivot+1,end)





# 코드를 작성하세요.


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)
