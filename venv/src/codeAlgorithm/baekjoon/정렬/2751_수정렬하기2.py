'''
  문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
  입력
  1) 첫째 줄 - 수의 개수(1<=N<=1000)
  2) 둘째 줄부터~ - 숫자(절댓값이 1000 이하인 정수), 중복 X

  해결법
  1) Merge sort - O(nlogn)
  2) Heap sort - O(nlogn)
'''

from sys import stdin

#병합정렬 구현 - Merge
def merge(left, right):
    merge_list = list()

    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0] < right[0]:
                merge_list.append(left.pop(0))
            elif left[0] > right[0]:
                merge_list.append(right.pop(0))
        elif len(left)>0 and len(right)==0:
            merge_list.append(left.pop(0))
        elif len(left)==0 and len(right)>0:
            merge_list.append(right.pop(0))

    return merge_list


#병합정렬 구현 - Divide
def merge_sort(numList):
    if len(numList) <= 1:
        return numList

    mid = len(numList)//2

    leftList = numList[:mid]
    rightList = numList[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


def solution():
    n = int(stdin.readline())
    numList = [0]*n

    for i in range(n):numList[i] = int(stdin.readline())

    result = merge_sort(numList)

    for n in result:
        print(n)

solution()