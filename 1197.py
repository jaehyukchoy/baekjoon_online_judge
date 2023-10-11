import sys,heapq
from collections import defaultdict
input=sys.stdin.readline
V,E=map(int,input().split())
g=defaultdict(dict)
for _ in range(E):
    A,B,C=map(int,input().split())
    g[A][B]=C
    g[B][A]=C

def prim(start):
    visited=[False]*(V+1)
    visited[start]=True
    q=[]
    total=0
    for k,i in g[start].items():
        heapq.heappush(q,(i,k))
    while q:
        w,v=heapq.heappop(q)
        if not visited[v]:
            visited[v]=True
            total+=w
            for vv,ww in g[v].items():
                heapq.heappush(q,(ww,vv))
    return total

print(prim(1))