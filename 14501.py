import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
t = []
p = []
for _ in range(n):
    _t, _p = map(int,input().split())
    t.append(_t)
    p.append(_p)
dp = defaultdict(int)
for i in range(n-1,-1,-1):
    if t[i] <= n-i:
        dp[i] = max(dp[i+t[i]] + p[i],dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])