"""
    시간복잡도 : O(n)
"""
def max_profit(stock_list):
    profit = 0
    for i in range(len(stock_list)-1):
        if i==0 or profit < max(stock_list[i+1:])-stock_list[i]:
            profit = max(stock_list[i+1:])-stock_list[i]
    return profit

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))

"""
    알게된 점
    1) list[:i]의 시간복잡도는 O(n^2)
    2) max(list)의 시간복잡도는 O(n)
"""