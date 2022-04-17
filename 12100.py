import sys
from collections import deque
from itertools import product
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
m = ['up', 'down', 'right', 'left']
def move(d):
    if d == 'up':
        for j in range(n):
            tmp = deque()
            for i in range(n):
                if b[i][j] != 0:
                    tmp.append(b[i][j])
            idx = 0
            while tmp:
                if len(tmp) == 1:
                    b[idx][j] = tmp.popleft()
                elif tmp[0] == tmp[1]:
                    b[idx][j] = tmp.popleft() + tmp.popleft()
                else:
                    b[idx][j] = tmp.popleft()
                idx += 1
            for i in range(idx, n):
                b[i][j] = 0
    elif d == 'down':
        for j in range(n):
            tmp = deque()
            for i in range(n-1, -1, -1):
                if b[i][j] != 0:
                    tmp.append(b[i][j])
            idx = n-1
            while tmp:
                if len(tmp) == 1:
                    b[idx][j] = tmp.popleft()
                elif tmp[0] == tmp[1]:
                    b[idx][j] = tmp.popleft() + tmp.popleft()
                else:
                    b[idx][j] = tmp.popleft()
                idx -= 1
            for i in range(idx, -1, -1):
                b[i][j] = 0
    elif d == 'right':
        for j in range(n):
            tmp = deque()
            for i in range(n-1, -1, -1):
                if b[j][i] != 0:
                    tmp.append(b[j][i])
            idx = n-1
            while tmp:
                if len(tmp) == 1:
                    b[j][idx] = tmp.popleft()
                elif tmp[0] == tmp[1]:
                    b[j][idx] = tmp.popleft() + tmp.popleft()
                else:
                    b[j][idx] = tmp.popleft()
                idx -= 1
            for i in range(idx, -1, -1):
                b[j][i] = 0
    elif d == 'left':
         for j in range(n):
            tmp = deque()
            for i in range(n):
                if b[j][i] != 0:
                    tmp.append(b[j][i])
            idx = 0
            while tmp:
                if len(tmp) == 1:
                    b[j][idx] = tmp.popleft()
                elif tmp[0] == tmp[1]:
                    b[j][idx] = tmp.popleft() + tmp.popleft()
                else:
                    b[j][idx] = tmp.popleft()
                idx += 1
            for i in range(idx, n):
                b[j][i] = 0

answer = 0
for mm in product(m, repeat = 5):
    b = deepcopy(board)
    for mmm in mm:
        move(mmm)
    test = []
    for i in range(n):
        test.append(max(b[i]))
    if answer < max(test):
        answer = max(test)
print(answer)
