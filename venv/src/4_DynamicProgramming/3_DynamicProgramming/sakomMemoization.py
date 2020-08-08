def max_profit_memo(price_list, count, cache):
    profit = 0
    # base case : 0,1개를 팔았을때 최대수익은 정해져있다.
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 캐시에 값이 존재한다면 값 리턴
    if count in cache:
        print("is profit -> %d"%cache.get(count))
        return cache.get(count)
    else:
        for i in range(count+1):
            if profit < price_list[count-i] + price_list[i]:
                print("%d %d => %d"%(count,i,(price_list[count-i] + price_list[i])))
                profit = price_list[count-i] + price_list[i]

def max_profit(price_list, count):
    max_profit_cache = {}
    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
# print(max_profit([0, 100, 400, 800, 900, 1000], 10))
# print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
