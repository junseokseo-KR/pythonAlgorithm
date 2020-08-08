def fib_tab(n):
    dic = {}
    for i in range(1,n+1):
        if i<3:
            dic[i] = 1
        else:
            dic[i] = dic.get(i-1)+dic.get(i-2)
    return dic.get(n)


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))