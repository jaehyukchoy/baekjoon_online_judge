import sys,heapq
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
l=0
r=n-1
ans=[]
while l<r:
    x=a[l]+a[r]
    heapq.heappush(ans,(abs(x),a[l],a[r]))
    if x==0:
        break
    elif x<0:
        l+=1
    else:
        r-=1
x,l,r=heapq.heappop(ans)
print(l,r)