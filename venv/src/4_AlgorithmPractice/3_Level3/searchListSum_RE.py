import time
start = time.time()
"""
    1) BruteForce 방식으로 풀이 -> O(n^2)
    2) in 사용 -> O(n^2)

"""

def sum_in_list(search_sum, sorted_list):
    high = len(sorted_list)-1
    low = 0

    while high!=low:
        sumVal = sorted_list[high]+sorted_list[low]
        if sumVal > search_sum:
            high-=1
        elif sumVal < search_sum:
            low+=1
        else:
            return True

    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
print("time : %s"%(time.time()-start))