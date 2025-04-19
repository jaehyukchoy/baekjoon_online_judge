import sys, math
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
k = int(input())

arr.sort() 

lengths = [len(s) for s in arr]
mods = [int(s) % k for s in arr]

pow10 = [1] * 51
for i in range(1, 51):
    pow10[i] = (pow10[i-1] * 10) % k

dp = [[0] * k for _ in range(1 << n)]
dp[0][0] = 1 

for used in range(1 << n):
    for mod in range(k):
        if dp[used][mod] == 0:
            continue

        prev = -1
        for i in range(n):
            if used & (1 << i):
                continue
            if arr[i] == prev:
                continue
            prev = arr[i]

            next_used = used | (1 << i)
            next_mod = (mod * pow10[lengths[i]] + mods[i]) % k
            dp[next_used][next_mod] += dp[used][mod]


bunza = dp[(1 << n) - 1][0]
bunmo = math.factorial(n)

counter = Counter(arr)
for v in counter.values():
    bunmo //= math.factorial(v)

g = math.gcd(bunza, bunmo)
print(f"{bunza//g}/{bunmo//g}")
