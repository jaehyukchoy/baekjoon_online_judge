import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def sol():
    res=[]
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        node=q.popleft()
        res.append(node)
        for i in graph[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    return res

ans=sol()
for a in ans:
    print(a,end=' ')
