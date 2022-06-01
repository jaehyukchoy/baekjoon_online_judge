import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
q = deque()
d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
for nn in range(n):
    for mm in range(m):
        if space[nn][mm] == 1:
            q.append((nn,mm))
while q:
    x,y = q.popleft()
    for dx,dy in d:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<m and space[nx][ny] == 0:
            space[nx][ny] = 1 + space[x][y]
            q.append((nx,ny))

print(max(map(max, space))-1)
