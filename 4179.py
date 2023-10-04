import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
miro=[[0]*c for _ in range(r)]
WALL=-1
FIRE=1
JIHOON=2
fireq=deque()
for i in range(r):
    tmp=input()
    for j in range(c):
        if tmp[j]=='#':
            miro[i][j]=WALL
        elif tmp[j]=='J':
            miro[i][j]=JIHOON
            jh=(i,j)
        elif tmp[j]=='F':
            miro[i][j]=FIRE
            fireq.append((i,j))

def fire():
    if fireq:
        qlen=len(fireq)
        for _ in range(qlen):
            x,y=fireq.popleft()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx=x+dx
                ny=y+dy
                if 0<=nx<r and 0<=ny<c and (miro[nx][ny]==0 or miro[nx][ny]==JIHOON):
                    miro[nx][ny]=FIRE
                    fireq.append((nx,ny))


def sol(q):
    before=-1
    while q:
        x,y,t=q.popleft()
        if check(x,y):
            return(t+1)
        if t!=before:
            fire()
            before=t
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<r and 0<=ny<c and miro[nx][ny]==0:
                miro[nx][ny]=JIHOON
                q.append((nx,ny,t+1))
    return -1

def check(x,y):
    if x==0 or x==r-1 or y==0 or y==c-1:
        return True
    return False


ans=sol(deque([(jh[0],jh[1],0)]))
if ans==-1:
    print('IMPOSSIBLE')
else:
    print(ans)