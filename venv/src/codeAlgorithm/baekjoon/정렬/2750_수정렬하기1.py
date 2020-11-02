'''
  문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
  입력
  1) 첫째 줄 - 수의 개수(1<=N<=1000)
  2) 둘째 줄부터~ - 숫자(절댓값이 1000 이하인 정수), 중복 X

  해결법
  1) Seletion sort - O(n²)
  2) Bubble sort - O(n²)
'''

from sys import stdin

#선택정렬 구현
def selection_sort(numList):
    print('Selection Sort : ',end='')
    for i in range(1, len(numList)):
        key = numList[i]
        j=i

        while j>0 and key<numList[j-1]:
            numList[j] = numList[j-1]
            j-=1

        numList[j] = key

    print(numList)

#거품정렬 구현
def bubble_sort(numList):
    print('Bubble Sort : ',end='')

    for i in range(len(numList)-1,0,-1):
        for j in range(i):
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]

    print(numList)




def solution():
    n = int(stdin.readline())
    numList = [0]*n

    for i in range(n):numList[i] = int(stdin.readline())

    # bubble_sort(numList)
    # selection_sort(numList)

    for n in result:
        print(n)

solution()