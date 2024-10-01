import sys
input=sys.stdin.readline
n=int(input())
point=[list(map(int,input().split())) for _ in range(n)]
point.sort()
ans=0
l,r=point[0]
for x,y in point[1:]:
    if x>r:
        ans+=r-l
        l,r=x,y
    elif x<=r:
        r=max(r,y)

print(ans+r-l)