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

"""
    시작 지점이 0일때
	잔여물의 양 = 용량-도착지점
그 이후 부터
	잔여물의 양 = 용량-(도착지점-시작지점)

잔여물의 양은 계속해서 초기화

문제점
	1. 잔여물의 양이 0보다 작을때, 즉 음수일때
도착지점과 시작지점의 인덱스 차이가 1밖에 나지 않을경우 무한루프가 발생한다.
		a. 중첩조건문을 이용해 인덱스 차이가 1보다 클 때만  시작지점을 종료지점-1로 지정

몰랐던 것
	1. 최적 부분 구조 파악
탐욕적 선택 속성 파악 
"""