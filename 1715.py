import sys,heapq
input=sys.stdin.readline
n=int(input())
q=[]
for _ in range(n):
    heapq.heappush(q,int(input()))
ans=0
while len(q)>1:
    a=heapq.heappop(q)
    b=heapq.heappop(q)
    t=a+b
    ans+=t
    heapq.heappush(q,t)
print(ans)