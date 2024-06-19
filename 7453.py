import sys
input = sys.stdin.readline
n = int(input())
a = []
b = []
c = []
d = []
for _ in range(n):
    _a, _b, _c, _d = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)
    d.append(_d)
ab = []
cd = []
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        cd.append(c[i]+d[j])
ab.sort()
cd.sort()
length = len(ab) - 1
ans = 0
left = 0
right = length
while left <= length and right >= 0:
    if ab[left] + cd[right] == 0:
        i = 1
        while left+i <= length and ab[left] == ab[left+i]:
            i += 1
        j = 1
        while right-j >= 0 and cd[right] == cd[right-j]:
            j += 1        
        ans += i * j
        left += i
        right -= j
    elif ab[left] + cd[right] < 0:
        left += 1
    else:
        right -= 1
print(ans)