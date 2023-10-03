import sys
from collections import defaultdict
from copy import deepcopy
input=sys.stdin.readline
n,k=map(int,input().split())
l=[tuple(map(int,input().split())) for _ in range(n)]
dp=[0]*(k+1)
dp_idx=defaultdict(set)
for i in range(1,k+1):
    for idx,(w,v) in enumerate(l):
        if 0<=i-w<=k and idx not in dp_idx[i-w]:
            if dp[i]<dp[i-w]+v:
                dp[i]=max(dp[i],dp[i-w]+v)
                tmp=deepcopy(dp_idx[i-w])
                tmp.add(idx)
                dp_idx[i]=tmp
print(max(dp))