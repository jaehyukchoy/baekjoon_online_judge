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
                visited[nx][ny]=True
                if cheese[nx][ny]==0:
                    q.append((nx,ny))
                else:
                    cheese[nx][ny]=0

time=0
before=0
while True:
    now = sum(map(sum,cheese))
    if now==0:
        break
    before=now
    time+=1
    melt()
print(time)
print(before)