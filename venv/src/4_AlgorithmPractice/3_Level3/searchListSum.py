import time
start = time.time()
"""
    1) BruteForce 방식으로 풀이 -> O(n^2)
    2) if문 사용 -> O(n)
"""
def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    for i in range(len(sorted_list)):
        if search_sum-sorted_list[i] in sorted_list:
            return True
    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))

"""
    in 함수는 O(n)이기 때문에 for문과 함께 쓰면 O(n^2)가 된다.
"""
print("time : %s"%(time.time()-start))