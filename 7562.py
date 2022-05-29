import sys
from collections import deque
input = sys.stdin.readline
move = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]

def bfs(b, queue, l, p, q):
    while queue:
        x, y = queue.popleft()
        if x == p and y == q:
            return b[x][y] - 1
            
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<l and 0<=ny<l and b[nx][ny] == 0:
                b[nx][ny] = b[x][y] + 1
                queue.append((nx,ny))
            

answer = []
for _ in range(int(input())):
    l = int(input())
    board = [[0]*l for __ in range(l)]
    x, y = map(int, input().split())
    p, q = map(int, input().split())
    board[x][y] = 1
    queue = deque()
    queue.append((x,y))
    answer.append(bfs(board,queue,l,p,q))

for a in answer:
    print(a)