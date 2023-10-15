import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
for _ in range(m):
    tmp=list(map(int,input().split()))
    for i in range(1,tmp[0]):
        g[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]]+=1

def sol():
    ret=[]
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        node=q.popleft()
        ret.append(node)
        for i in g[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    return ret

ans=sol()
if len(ans)<n:
    print(0)
else:
    for a in ans:
        print(a)
