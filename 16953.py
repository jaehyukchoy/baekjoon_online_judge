from collections import deque

A, B = map(int, input().split())

q = deque([(A, 1)])
v = set()
ans = -1
while q:
    now, depth = q.popleft()
    if now == B:
        ans = depth
        break
    v.add(now)
    for next in [now * 2, int(str(now) + "1")]:
        if next not in v and next <= B:
            q.append((next, depth + 1))

print(ans)
