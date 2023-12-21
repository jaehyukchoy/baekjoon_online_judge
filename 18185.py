n=int(input())
a=list(map(int,input().split()))
ans=0
i=0
for i in range(n-2):
    if a[i+1]<=a[i+2]:
        t=min(a[i],a[i+1])
        ans+=7*t
        a[i]-=t
        a[i+1]-=t
        a[i+2]-=t

        t=min(a[i],a[i+1])
        ans+=5*t
        a[i]-=t
        a[i+1]-=t

    else:
        t=min(a[i],a[i+1]-a[i+2])
        ans+=5*t
        a[i]-=t
        a[i+1]-=t

        t=min(a[i],a[i+1],a[i+2])
        ans+=7*t
        a[i]-=t
        a[i+1]-=t
        a[i+2]-=t
    
t=min(a[n-2],a[n-1])
ans+=5*t
a[n-2]-=t
a[n-1]-=t

ans+=sum(a)*3
print(ans)