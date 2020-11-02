def max_profit_memo(price_list, count, cache):
    profit = 0
    # base case : 0,1개를 팔았을때 최대수익은 정해져있다.
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 캐시에 값이 존재한다면 값 리턴
    if count in cache:
        return cache.get(count)

    # 팔아야할 개수가 리스트의 길이보다 크면 수익은 0
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0


    for i in range(1,int(count/2)+1):
        profit = max(profit,max_profit_memo(price_list,i,cache)+max_profit_memo(price_list,count-i,cache))

    cache[count] = profit
    return profit

def max_profit(price_list, count):
    max_profit_cache = {}
    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
