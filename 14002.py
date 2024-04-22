n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
s = [[aa] for aa in a]

for i in range(1, n):
    tmp = []
    for j in range(i):
        if a[j] < a[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                tmp = s[j]
    s[i] += tmp
print(max(dp))
print(*s[dp.index(max(dp))][::-1])
