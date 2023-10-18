import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]
ice=defaultdict(int)
for i in range(n):
    for j in range(m):
        if g[i][j]!=0:
            ice[(i,j)]=g[i][j]

def melt():
    to_melt=defaultdict(int)
    for (x,y),i in ice.items():
        cnt=0
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if g[x+dx][y+dy]==0:
                cnt+=1
        to_melt[(x,y)]=cnt
    for (x,y),c in to_melt.items():
        ice[(x,y)]-=c
        g[x][y]=ice[(x,y)]
        if ice[(x,y)]<=0:
            del ice[(x,y)]
            g[x][y]=0

def dfs(p,q):
    visited[p][q]=True
    for dp,dq in [(1,0),(0,1),(-1,0),(0,-1)]:
        np=p+dp
        nq=q+dq
        if 0<=np<n and 0<=nq<m and not visited[np][nq] and g[np][nq]!=0:
            dfs(np,nq)

ans=0
flag=True

while flag:
    ans+=1
    melt()
    if not ice:
        ans=0
        break
    else:
        visited=[[False]*m for _ in range(n)]
        for (x,y),i in ice.items():
            dfs(x,y)
            break
        for (x,y),i in ice.items():
            if visited[x][y]==False:
                flag=False
                break
            
print(ans)