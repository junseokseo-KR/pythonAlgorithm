def fib_memo(n, cache):
    # base case
    if n<3:
        return 1

    if cache.get(n) != None:
        return cache.get(n)
    else:
        cache[n] = fib_memo(n-1,cache)+fib_memo(n-2,cache)
        return cache.get(n)

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    return fib_memo(n,fib_cache)
# 테스트
print(fib(8))
print(fib(53))
print(fib(213))