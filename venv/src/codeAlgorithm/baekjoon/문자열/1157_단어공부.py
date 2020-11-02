import sys

'''
    답 리턴 변수 answer
    입력 받을 변수 str
    알파벳들이 들어갈 딕셔너리 alphaDic
'''
answer = ""
str = sys.stdin.readline().rstrip()
alphaDic = {}

'''
    문자의 길이만큼 반복하여
    스펠링을 대문자화 시킨다.
    
    스펠링이 알파벳 딕셔녀리에 키값으로 존재하지 않으면 해당 키의 1 값을 추가한다.
    존재하면 값을 1추가한다.
'''
for c in str:
    C = c.upper()

    if C not in alphaDic.keys():
        alphaDic[C] = 1
    else:
        alphaDic[C]+=1

'''
    알파벳 딕셔너리의 값들중 최대값을 찾는다.
    딕셔너리의 키의 값을 탐색하며 해당 최대값을 가지고 있는 키 값을 리턴 문자열에 추가한다.
'''
maxVal = max(alphaDic.values())

for key in alphaDic.keys():
    if alphaDic[key] == maxVal:
        answer+=key

'''
    문자열의 길이가 1보다 크면 ? 를 출력하고 1이면 해당 스펠링만 출력한다.
'''
if len(answer) > 1:
    print("?")
else:
    print(answer)

'''
다른 사람의 풀이
모두 대문자화 하여 입력받는다.
word = input().upper()

li = [0] * (ord('Z') + 1)
for ab in range(ord('A'), ord('Z')+1):
    li[ab] = word.count(chr(ab))

max_ = max(li[ord('A'):])
if li[ord('A'):].count(max_) >= 2:
    print('?')
else:
    print(chr(li.index(max_)))
    
ord 함수 : 문자의 아스키코드 값을 돌려주는 함수
'''