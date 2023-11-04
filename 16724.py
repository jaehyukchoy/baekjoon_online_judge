import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
g=[list(input().strip()) for _ in range(n)]
v=[[0]*m for _ in range(n)]
zone=0
move={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
def dfs(x,y):
    global zone
    v[x][y]=1
    dx,dy=move[g[x][y]]
    nx,ny=x+dx,y+dy
    if v[nx][ny]==1:
        zone+=1
    elif v[nx][ny]==0:
        dfs(nx,ny)
    v[x][y]=2

for i in range(n):
    for j in range(m):
        if v[i][j]==0:
            dfs(i,j)
print(zone)