n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
for i in range(n - 2, -1, -1):
    t = max(1 + a[i] - a[i + 1], 0)
    a[i] -= t
    ans += t
print(ans)
