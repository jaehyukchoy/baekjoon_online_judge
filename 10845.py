import sys
from collections import deque
input = sys.stdin.readline
q = deque()
answer = []
for _ in range(int(input())):
    com = input().split()
    if com[0] == 'push':
        q.append(com[1])
    elif com[0] == 'pop':
        if q:
            answer.append(q.popleft())
        else:
            answer.append(-1)
    elif com[0] == 'size':
        answer.append(len(q))
    elif com[0] == 'empty':
        if q:
            answer.append(0)
        else:
            answer.append(1)
    elif com[0] == 'front':
        if q:
            answer.append(q[0])
        else:
            answer.append(-1)
    elif com[0] == 'back':
        if q:
            answer.append(q[-1])
        else:
            answer.append(-1)
for a in answer:
    print(a)