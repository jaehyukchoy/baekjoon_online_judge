import sys,heapq
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=a[0]+a[1]+a[2]
for i in range(n-2):
    l=i+1
    r=n-1
    while l<r:
        t=a[i]+a[l]+a[r]
        if abs(ans)>=abs(t):
            x,y,z=a[i],a[l],a[r]
            ans=t
        if t==0:
            break
        elif t<0:
            l+=1
        else:
            r-=1
print(x,y,z)