import sys,heapq
input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(n+1)
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    indegree[b]+=1

def topology_sort():
    res=[]
    q=[]
    for i in range(1,n+1):
        if indegree[i]==0:
            heapq.heappush(q,i)
    while q:
        cur=heapq.heappop(q)
        res.append(cur)
        for i in g[cur]:
            indegree[i]-=1
            if indegree[i]==0:
                heapq.heappush(q,i)
    return res
ans=topology_sort()
for a in ans:
    print(a,end=' ')