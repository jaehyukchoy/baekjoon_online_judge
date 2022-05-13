import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n+2)] for _ in range(n+2)]
for x in range(n+2):
    for y in range(n+2):
        if x == 0 or x == n+1 or y == 0 or y == n+1 or (x == 1 and y == 1):
            board[x][y] = -1

for _ in range(int(input())):
    kx, ky = map(int,input().split())
    board[kx][ky] = 1

l = deque()
for _ in range(int(input())):
    l.append(input().split())

headx = 1
heady = 1
tailx = 1
taily = 1
mov = [(0,1),(1,0),(0,-1),(-1,0)]
mov_idx = 0
mov_his = deque()
time = 0
if l:
    x, c = l.popleft()
while True:
    time += 1
    movx, movy = mov[mov_idx]
    mov_his.append((movx,movy))
    headx += movx
    heady += movy
    if board[headx][heady] == -1:
        print(time)
        break
    elif board[headx][heady] == 0:
        board[tailx][taily] = 0
        tx, ty = mov_his.popleft()
        tailx += tx
        taily += ty
    board[headx][heady] = -1
    if time >= int(x):
        if c == 'D':
            mov_idx += 1
            mov_idx %= 4
        elif c == 'L':
            mov_idx += -1
            if mov_idx == -1:
                mov_idx = 3
        if l:
            x, c = l.popleft()
        else:
            x = sys.maxsize