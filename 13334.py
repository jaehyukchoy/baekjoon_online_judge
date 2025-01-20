import heapq
from collections import defaultdict

q = []
n = int(input())
for _ in range(n):
    h, o = map(int, input().split())
    if h <= o :
        left, right = h, o
    else:
        left, right = o, h
    heapq.heappush(q, (right, left))
d = int(input())


p = []
cnt = 0
ans = 0
while q:
    right, left = heapq.heappop(q)
    if left >= right - d:
        cnt += 1
        heapq.heappush(p, (left, right))
    while p:
        l, r = heapq.heappop(p)
        if l >= right - d:
            heapq.heappush(p, (l, r))
            break
        else:
            cnt -= 1
    ans = max(ans, cnt)
print(ans)