import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input=sys.stdin.readline
v=int(input())
graph=defaultdict(list)
for _ in range(v):
    tmp=list(map(int,input().split()))
    p=tmp[0]
    i=1
    while tmp[i]!=-1:
        graph[p].append([tmp[i],tmp[i+1]])
        i+=2

def dfs(p,distance):
    global diameter
    global farnode
    if diameter<distance:
        diameter=distance
        farnode=p
    visited[p]=True
    for node,d in graph[p]:
        if not visited[node]:
            dfs(node,distance+d)

diameter=0

visited=[False]*(v+1)
dfs(1,0)
visited=[False]*(v+1)
dfs(farnode,0)

print(diameter)