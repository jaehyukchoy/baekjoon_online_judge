m = 0
ans = 0
for i in range(1, 10):
    n = int(input())
    if n > m:
        m = n
        ans = i
print(m)
print(ans)