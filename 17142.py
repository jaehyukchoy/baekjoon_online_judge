from itertools import combinations
from collections import deque
n,m=map(int,input().split())
lab=[list(map(int,input().split())) for _ in range(n)]

virus=set()
for i in range(n):
    for j in range(n):
        if lab[i][j]==2:
            virus.add((i,j))

def bfs(q):
    v=[[False]*n for _ in range(n)]
    ret=0
    while q:
        x,y,d=q.popleft()
        if lab[x][y]==2:
            ret=min(ret,d)
        else:
            ret=d
        v[x][y]=True
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<n and lab[nx][ny]!=1 and not v[nx][ny]:
                q.append((nx,ny,d+1))
                v[nx][ny]=True
    
    

    for i in range(n):
        for j in range(n):
            if not v[i][j] and lab[i][j]!=1 and (i,j) not in virus:
                return ret,False
    return ret,True


ans=n**2
flag=False
for v in combinations(virus,m):
    q=deque()
    for vx,vy in v:
        q.append((vx,vy,0))
    d,f=bfs(q)
    if f:
        ans=min(ans,d)
        flag=True

if flag:
    print(ans)
else:
    print(-1)