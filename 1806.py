import sys
input=sys.stdin.readline
n,s=map(int,input().split())
a=list(map(int,input().split()))
x=0
r=0
ans=n+1
for l in range(n):
    while x<s and r<n:
        x+=a[r]
        r+=1
    if x>=s:
        ans=min(ans,r-l)
    x-=a[l]
if ans==n+1:
    ans=0
print(ans)