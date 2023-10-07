import sys
from collections import deque
input=sys.stdin.readline
w,h=map(int,input().split())
m=[[0]*w for _ in range(h)]
lazer=[]
for i in range(h):
    tmp=input()
    for j in range(w):
        if tmp[j]=='C':
            lazer.append((i,j))
        elif tmp[j]=='*':
            m[i][j]=-1

def com(start,end):
    q=deque([(start[0],start[1],0)])
    v=[[-1]*w for _ in range(h)]
    v[start[0]][start[1]]=0
    while q:
        x,y,c=q.popleft()
        if (x,y)==end:
            return v[x][y]
        for dx,dy in [(1,0),(0,-1),(-1,0),(0,1)]:
            i=0
            while True:
                i+=1
                nx=x+dx*i
                ny=y+dy*i
                if nx<0 or nx>=h or ny<0 or ny>=w or m[nx][ny]==-1:
                    break
                if v[nx][ny]==-1:
                    v[nx][ny]=c
                    q.append((nx,ny,c+1))
print(com(lazer[0],lazer[1]))