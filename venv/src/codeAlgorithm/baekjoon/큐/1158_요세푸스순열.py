'''
  - 문제
  요세푸스 문제는 다음과 같다.
  1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
  이제 순서대로 K번째 사람을 제거한다.
  한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
  이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
  원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
  예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

  N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

  - 출력
  1) 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

  - 해결방법
  1) n까지의 원소가 들어있는 que를 생성한다. [O(N)]
  2) que의 크기가 1이 될때 까지 loop
'''

from sys import stdin
from sys import stdout
from collections import deque

n,k = map(int, stdin.readline().split())
que = deque([i+1 for i in range(n)])
cnt = k-1
stdout.write(f'<')
while len(que)>1:
    stdout.write(f'{que[cnt]}, ')
    del que[cnt]

    cnt-=1
    if cnt<=len(que): cnt+=k
    while cnt>=len(que): cnt=cnt-len(que)

# 마지막 제거
stdout.write(f'{que.pop()}>\n')