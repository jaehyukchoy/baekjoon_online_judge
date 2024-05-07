n, c = map(int, input().split())
arr = []
for _ in range(int(input())):
    x, y, a = map(int, input().split())
    arr.append((x, y, a))

arr.sort(key=lambda x: x[1])

cargo = [0] * (n + 1)
ans = 0
for x, y, a in arr:
    for i in range(x, y):
        a = min(a, c - cargo[i])
    for i in range(x, y):
        cargo[i] += a
    ans += a
print(ans)
