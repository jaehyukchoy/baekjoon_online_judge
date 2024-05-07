n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    tmp = a[:i] + a[i + 1 :]
    left = 0
    right = n - 2
    while left < right:
        if tmp[left] + tmp[right] > a[i]:
            right -= 1
        elif tmp[left] + tmp[right] < a[i]:
            left += 1
        else:
            ans += 1
            break

print(ans)
