# 행복수와 슬픈수를 중복없이 담기 위한 집합자료형
happySet = set([1])
sadSet = set([])

# 자릿수의 합을 return 하는 함수
def return_digit_sum(n):
    sum = 0
    while n != 0:
        sum += int(n % 10)**2
    n //= 10
    return sum

# 행복수를 찾기 위한 재귀함수
def find_happyNum(n, arr = []):
    # 행복수 집합에 n이 존재한다면
    if n in happySet:
        # 이전 값들을 포함하여 행복수 집합에 중복없이 update하고 True 반환
        happySet.update(arr)
        return True
    # 슬픈수 집합에 n이 존재한다면
    elif n in arr or n in sadSet:
        # 이전 값들을 포함하여 슬픈수 집합에 중복없이 update하고 False 반환
        sadSet.update(arr)
        return False
    # 두 집합에 존재하지 않는 수라면
    else:
        # 함수내 배열에 삽입 후 해당 자릿수의 합으로 재귀
        arr.append(n)
        return find_happyNum(return_digit_sum(n), arr)


def solution(n):
    answer = []
    #n까지 loop를 돌며 True 값이 반환 된다면 해당 인덱스를 해답 배열에 추가
    for i in range(1, n + 1):
        if find_happyNum(i,[]):
            answer.append(i)

    print(f'1~{n} 범위의 행복 수는 {len(answer)}개이고 총합은 {sum(answer)}입니다.')


solution(9)