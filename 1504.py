import sys, heapq, math
from collections import defaultdict
input=sys.stdin.readline
n,e=map(int,input().split())
g=defaultdict(dict)
for _ in range(e):
    a,b,c=map(int,input().split())
    g[a][b]=c
    g[b][a]=c
v1,v2=map(int,input().split())

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

d1=dijkstra(1)
dv1=dijkstra(v1)
dv2=dijkstra(v2)
a1=a2=-1
if v1 in d1 and v2 in dv1 and n in dv2:
    a1=dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[n]
if v2 in d1 and v1 in dv2 and n in dv1:
    a2=dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[n]
if a1==a2==-1:
    print(-1)
elif a1==-1 and a2!=-1:
    print(a2)
elif a1!=-1 and a2==-1:
    print(a1)
else:
    print(min(a1,a2))