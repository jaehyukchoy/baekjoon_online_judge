import sys
input=sys.stdin.readline
a=input().rstrip()
b=input().rstrip()
bb=[]
for i in range(len(b)):
    bb.append(b[i:])
ans=0
for b in bb:
    al=len(a)
    bl=len(b)
    dp=[[0]*(bl+1) for _ in range(al+1)]
    for ai in range(1,al+1):
        for bi in range(1,bl+1):
            if a[ai-1]==b[bi-1]:
                dp[ai][bi]=dp[ai-1][bi-1]+1
            else:
                dp[ai][bi]=max(dp[ai-1][bi],dp[ai][bi-1])
    ans+=sum(map(sum,dp))
print(ans)