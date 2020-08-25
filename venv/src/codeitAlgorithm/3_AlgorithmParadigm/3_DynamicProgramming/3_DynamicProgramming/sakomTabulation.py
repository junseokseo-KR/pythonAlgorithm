def max_profit(price_list, count):
    proList = {}
    # 코드를 작성하세요.
    for i in range(count+1):
        if proList.get(i) == None:
            price_list.append(0)
            proList[i] = 0
        for j in range(int(i/2)+1):
            if i <= count:
                proList[i] = max(proList[i],price_list[i-j]+price_list[j])
        price_list[i] = proList[i]
    return proList.get(count)

# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
