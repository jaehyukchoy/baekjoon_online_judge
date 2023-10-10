import sys,math,heapq
from collections import defaultdict
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
g=defaultdict(dict)
for _ in range(E):
    u,v,w=map(int,input().split())
    if v in g[u]:
        g[u][v]=min(w,g[u][v])
    else:
        g[u][v]=w

def dijkstra(start):
    d={node:math.inf for node in range(1,V+1)}
    d[start]=0
    q=[]
    heapq.heappush(q,(d[start],start))
    while q:
        dd,n=heapq.heappop(q)
        if d[n]<dd:
            continue
        for adj,t in g[n].items():
            if t+dd<d[adj]:
                d[adj]=t+dd
                heapq.heappush(q,(t+dd,adj))
    return d

for key,item in dijkstra(K).items():
    if item==math.inf:
        print('INF')
    else:
        print(item)
