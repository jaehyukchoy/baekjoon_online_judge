import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
g=[list(input().rstrip()) for _ in range(n)]

def make_group(x,y,gnum):
    g[x][y]=gnum
    q=deque([(x,y)])
    ret=0
    while q:
        ret+=1
        i,j=q.popleft()
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<n and 0<=nj<m and g[ni][nj]=='0':
                q.append((ni,nj))
                g[ni][nj]=gnum
    return ret

group=dict()
gnum=2
for i in range(n):
    for j in range(m):
        if g[i][j]=='0':
            group[gnum]=make_group(i,j,gnum)
            gnum+=1

ans=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j]=='1':
            gset=set()
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                ni,nj=i+di,j+dj
                if 0<=ni<n and 0<=nj<m and g[ni][nj]!='1':
                    gset.add(g[ni][nj])
            cnt=1
            for gs in gset:
                cnt+=group[gs]
            ans[i][j]=cnt%10
for an in ans:
    for a in an:
        print(a,end='')
    print()