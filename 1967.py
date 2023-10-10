import sys
from collections import defaultdict
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
graph=defaultdict(dict)
for _ in range(n-1):
    parent,child,w=map(int,input().split())
    graph[parent][child]=w
    graph[child][parent]=w

def dfs(p,distance):
    global diameter
    global farnode
    if diameter<distance:
        diameter=distance
        farnode=p
    visited[p]=True
    for node,d in graph[p].items():
        if not visited[node]:
            dfs(node,distance+d)

diameter=0
farnode=1
visited=[False]*(n+1)
dfs(1,0)
visited=[False]*(n+1)
dfs(farnode,0)

print(diameter)