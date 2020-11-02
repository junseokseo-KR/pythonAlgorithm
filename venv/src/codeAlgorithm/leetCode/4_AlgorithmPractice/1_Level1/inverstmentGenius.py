def sublist_max(profits):
    profit_list = []
    maxValue = 0
    # 코드를 작성하세요.
    for i in range(len(profits)):
        sum = 0
        for j in range(i,len(profits)):
            sum += profits[j]
            if sum > maxValue:
                maxValue = sum
    return maxValue
# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]))