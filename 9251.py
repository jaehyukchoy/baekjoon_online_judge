a=input()
b=input()
al=len(a)
bl=len(b)
dp=[[0]*(bl+1) for _ in range(al+1)]
for ai in range(1,al+1):
    for bi in range(1,bl+1):
        if a[ai-1]==b[bi-1]:
            dp[ai][bi]=max(dp[ai-1][bi-1]+1,dp[ai-1][bi],dp[ai][bi-1])
        else:
            dp[ai][bi]=max(dp[ai-1][bi],dp[ai][bi-1])
print(dp[al][bl])