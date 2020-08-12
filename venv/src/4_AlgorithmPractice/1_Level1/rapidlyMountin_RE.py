def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    course = []
    start, end, water = 0, 0, capacity

    while end != len(water_stops):
        if start == 0:
            water -= water_stops[end]

        else:
            water -= (water_stops[end] - water_stops[start])

        if water > 0:
            end += 1
        else:
            if water < 0:
                if end-start > 1:
                    start = end - 1
                else:
                    start = end
                    course.append(water_stops[start-1])
            else:
                start = end
            end = start + 1
            course.append(water_stops[start])
        water = capacity
    course.append(water_stops[len(water_stops) - 1])
    print(course)


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
