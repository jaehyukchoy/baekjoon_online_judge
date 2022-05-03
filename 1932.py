import sys
input = sys.stdin.readline
n = int(input())
dp = []
for i in range(n):
    t = list(map(int,input().split()))
    if i==0:
        dp.append(t)
    else:
        tmp = []
        for j in range(len(t)):
            if j==0:
                tmp.append(dp[i-1][j]+t[j])
            elif j==len(t)-1:
                tmp.append(dp[i-1][j-1]+t[j])
            else:
                tmp.append(max(dp[i-1][j-1],dp[i-1][j])+t[j])
        dp.append(tmp)
print(max(dp[-1]))