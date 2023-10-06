import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
cave=[['.']*c for _ in range(r)]
for i in range(r):
    t=input()
    for j in range(c):
        if t[j]=='x':
            cave[i][j]='x'
n=int(input())
h=list(map(int,input().split()))


def cluster(start):
    q=deque([start])
    ct=deque([start])
    v=[[False]*c for _ in range(r)]
    v[start[0]][start[1]]=True
    
    while q:
        x,y=q.popleft()
        if x==r-1:
            return False
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<r and 0<=ny<c and not v[nx][ny] and cave[nx][ny]=='x':
                q.append((nx,ny))
                ct.append((nx,ny))
                v[nx][ny]=True
    return ct

def fall(ct):
    if not ct:
        return
    for x,y in ct:
        cave[x][y]='.'
    l=1
    flag=True
    while flag:
        for x,y in ct:
            if x+l>=r or cave[x+l][y]=='x':
                flag=False
                break
        if flag:
            l+=1
    for x,y in ct:
        cave[x+l-1][y]='x'
    

for idx, hh in enumerate(h):
    check=deque()
    if idx%2==0:
        for p in range(c):
            if cave[r-hh][p]=='x':
                cave[r-hh][p]='.'
                for dx,dy in [(1,0),(-1,0),(0,1)]:
                    nx=r-hh+dx
                    ny=p+dy
                    if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x':
                        check.append((nx,ny))
                break
    else:
        for p in range(c-1,-1,-1):
            if cave[r-hh][p]=='x':
                cave[r-hh][p]='.'
                for dx,dy in [(1,0),(-1,0),(0,-1)]:
                    nx=r-hh+dx
                    ny=p+dy
                    if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x':
                        check.append((nx,ny))
                break
    
    
    ct=[]
    while not ct and check:
        ct=cluster(check.pop())
    fall(ct)
    
for cv in cave:
    print(''.join(cv))