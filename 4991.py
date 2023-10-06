import sys
input=sys.stdin.readline
from collections import deque
from itertools import permutations

def clean(start):
    q=deque([start])
    v=[[-1]*w for _ in range(h)]
    v[start[0]][start[1]]=0
    while q:
        x,y=q.popleft()
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<h and 0<=ny<w and v[nx][ny]==-1 and room[nx][ny]!=-1:
                v[nx][ny]=v[x][y]+1
                q.append((nx,ny))
    return v


while True:
    w,h=map(int,input().split())
    if w==0:
        break
    room=[[0]*w for _ in range(h)]
    dirty=[]
    for i in range(h):
        tmp=input()
        for j in range(w):
            if tmp[j]=='*':
                room[i][j]=1
                dirty.append((i,j))
            elif tmp[j]=='x':
                room[i][j]=-1
            elif tmp[j]=='o':
                cleaner=(i,j)

    available=True
    l=dict()
    l[cleaner]=clean(cleaner)
    for i in range(h):
        for j in range(w):
            if l[cleaner][i][j]==-1 and room[i][j]!=-1:
                available=False
                break
        if not available:
            break
    if not available:
        print(-1)
    else:
        ans=400
        for d in dirty:
            l[d]=clean(d)
        for d_list in permutations(dirty):
            tmp=0
            p=cleaner
            for dx,dy in d_list:
                tmp+=l[p][dx][dy]
                p=(dx,dy)
            ans=min(ans,tmp)
        print(ans)