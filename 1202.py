import sys,heapq
input=sys.stdin.readline
N,K=map(int,input().split())
jewerly=[]
for _ in range(N):
    M,V=map(int,input().split())
    jewerly.append((M,V))
jewerly.sort()
bag=[int(input()) for _ in range(K)]
bag.sort()
ans=0
jew_idx=0
h=[]
for b in bag:
    while jew_idx<N and jewerly[jew_idx][0]<=b:
        heapq.heappush(h,-jewerly[jew_idx][1])
        jew_idx+=1
    if h:
        ans+=heapq.heappop(h)
print(-ans)