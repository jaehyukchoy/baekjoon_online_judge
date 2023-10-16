import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[1]*(n+1)
backup=[(0,0)]
for i in range(1,n+1):
    if i==1:
        backup.append((1,a[i-1]))
    else:
        if backup[-1][1]<a[i-1]:
            dp[i]=backup[-1][0]+1
            backup.append((dp[i],a[i-1]))
        else:
            l=0
            r=len(backup)-1
            while l<=r:
                m=(l+r)//2
                if backup[m][1]>=a[i-1]:
                    r=m-1
                else:
                    l=m+1
            p,q=backup[l]
            backup[l]=(p,a[i-1])
            dp[i]=p
print(max(dp))