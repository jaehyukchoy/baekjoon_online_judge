import sys
from collections import deque

r,c=map(int,sys.stdin.readline().split())
lake=[[0]*c for _ in range(r)]
for i in range(r):
    tmp=sys.stdin.readline()
    for j in range(c):
        if tmp[j]=='X':
            lake[i][j]=1
        elif tmp[j]=='L':
            lake[i][j]=2
            swan=(i,j)


d=[(1,0),(0,1),(-1,0),(0,-1)]
def bfs(q):
    nextq=deque()
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if 0<=nx<r and 0<=ny<c and not v[nx][ny]:
                if lake[nx][ny]==0:
                    v[nx][ny]=True
                    q.append((nx,ny))
                elif lake[nx][ny]==1:
                    nextq.append((x,y))
                else:
                    return []
    return nextq

def melt():
    q_len=len(meltq)
    for _ in range(q_len):
        x,y=meltq.popleft()
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if 0<=nx<r and 0<=ny<c and lake[nx][ny]==1:
                lake[nx][ny]=0
                meltq.append((nx,ny))


def first_melt():
    firstq=set()
    for i in range(r):
        for j in range(c):
            if lake[i][j]!=1:
                for di,dj in d:
                    ni=i+di
                    nj=j+dj
                    if 0<=ni<r and 0<=nj<c and lake[ni][nj]==1:
                        firstq.add((i,j))
                        break
    return deque(firstq)


ans=0
meltq=first_melt()
q=deque([swan])
v=[[False]*c for _ in range(r)]
v[swan[0]][swan[1]]=True
while True:
    q=bfs(q)
    if not q:
        print(ans)
        break
    melt()
    ans+=1

