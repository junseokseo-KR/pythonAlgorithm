def consecutive_sum(start, end):
    mid = int((end + start) / 2)
    if end == start:
        return start
    else:
        if end - start != 1:
            return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)
        elif end - start == 1:
            return end + start


# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))