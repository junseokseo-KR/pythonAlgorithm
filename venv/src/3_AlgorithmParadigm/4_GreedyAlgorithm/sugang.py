def course_selection(course_list):
    best_list = []
    course_list = sorted(course_list)
    bestIdx = 0
    select = 0
    firstValue = 24
    # 코드를 작성하세요.
    """
        1. 가장 먼저 끝나는 시간부터 고른다.
    """
    for i in range(len(course_list)):
        if course_list[i][1] < firstValue:
            firstValue = course_list[i][1]
            bestIdx = i

    best_list.append(course_list[bestIdx])

    select = bestIdx + 1
    while select != len(course_list):
        if course_list[bestIdx][1] < course_list[select][0] and course_list[bestIdx][1] < course_list[select][1]:
            best_list.append(course_list[select])
            bestIdx = select
        select += 1

    return best_list


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
