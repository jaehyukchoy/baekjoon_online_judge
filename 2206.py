import sys
from collections import deque
from copy import deepcopy
n,m=map(int,input().split())
g=[list(map(int,list(input()))) for _ in range(n)]
move=[(1,0),(-1,0),(0,1),(0,-1)]
v=[[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][0]=1
q=deque()
q.append((0,0,0))
while q:
    x,y,b=q.popleft()
    if x==n-1 and y==m-1:
        print(v[x][y][b])
        exit()
    for dx,dy in move:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m:
            if g[nx][ny]==0 and v[nx][ny][b]==0:
                q.append((nx,ny,b))
                v[nx][ny][b]=v[x][y][b]+1
            elif g[nx][ny]==1 and b==0:
                q.append((nx,ny,1))
                v[nx][ny][1]=v[x][y][0]+1
print(-1)