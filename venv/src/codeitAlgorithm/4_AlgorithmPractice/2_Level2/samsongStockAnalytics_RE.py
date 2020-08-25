"""
    알게된 점
    1) list[:i]의 시간복잡도는 O(n^2)
    2) max(list)의 시간복잡도는 O(n)
"""
def max_profit(stock_list):
    max_profit_val = stock_list[1]-stock_list[0]
    min_profit_val = min(stock_list[0], stock_list[1])

    for i in range(2,len(stock_list)-1):
        max_profit_val = max(max_profit_val,stock_list[i]-min_profit_val)
        min_profit_val = min(min_profit_val, stock_list[i])

    return max_profit_val

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))

