import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
cheese=[list(map(int,input().split())) for _ in range(n)]

def melt():
    q=deque([(0,0)])
    visited=[[False]*m for _ in range(n)]
    visited[0][0]=True
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if cheese[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                elif cheese[nx][ny]==1:
                    cheese[nx][ny]=2
                elif cheese[nx][ny]==2:
                    cheese[nx][ny]=3
    for i in range(n):
        for j in range(m):
             if cheese[i][j]==2:
                 cheese[i][j]=1
             elif cheese[i][j]==3:
                 cheese[i][j]=0

time=0
while sum(map(sum,cheese))>0:
    time+=1
    melt()
print(time)