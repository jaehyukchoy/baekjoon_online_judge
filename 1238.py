import sys
import heapq
import math
from collections import defaultdict
input=sys.stdin.readline
n,m,x=map(int,input().split())
g=defaultdict(dict)
for i in range(m):
    s,e,t=map(int,input().split())
    g[s][e]=t

def dijkstra(start):
    d={node:math.inf for node in g}
    d[start]=0
    q=[]
    heapq.heappush(q,(d[start],start))
    while q:
        dd,n=heapq.heappop(q)
        if d[n]<dd:
            continue
        for adj,t in g[n].items():
            if dd+t<d[adj]:
                d[adj]=dd+t
                heapq.heappush(q,(dd+t,adj))
    return d

to_home=dijkstra(x)
ans=0
for i in range(1,n+1):
    to_x=dijkstra(i)
    ans=max(ans,to_x[x]+to_home[i])
print(ans)

