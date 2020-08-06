def fib_memo(n, cache):
    return cache.get(n-1)


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    if n==1 or n==2:
        fib_cache = {n, 1}
    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))