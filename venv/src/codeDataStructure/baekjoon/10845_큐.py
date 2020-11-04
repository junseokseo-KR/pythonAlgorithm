from sys import stdin
from sys import stdout

class Que:
    def __init__(self):
        self.que = list()
        self.cnt = 0

    def push(self, n):
        self.que.append(n)
        self.cnt+=1

    def pop(self):
        if self.cnt:
            pop_num = self.que[0]
            self.que=self.que[1:]
            self.cnt-=1
            return pop_num
        return -1

    def front(self):
        if self.cnt:
            return self.que[0]
        return -1

    def back(self):
        if self.cnt:
            return self.que[self.cnt-1]
        return -1

    def size(self):
        return self.cnt

    def empty(self):
        if self.cnt:
            return 0
        else:
            return 1

n = int(stdin.readline())
que = Que()
for _ in range(n):
    command = list(map(str, stdin.readline().split()))
    if len(command)<2:
        if command[0]=='front':
            print(que.front())
        elif command[0]=='back':
            print(que.back())
        elif command[0]=='size':
            print(que.size())
        elif command[0]=='pop':
            print(que.pop())
        elif command[0]=='empty':
            print(que.empty())
    else:
        if command[0]=='push':
            que.push(int(command[1]))