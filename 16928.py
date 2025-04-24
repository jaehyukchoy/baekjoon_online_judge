from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
good, bad = {}, {}
for _ in range(n):
    x, y = map(int, input().split())
    good[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    bad[u] = v

visited = [False] * 101
visited[1] = True
q = deque([(1, 0)])
while q:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        break
    for dice in range(1, 7):
        next = now + dice
        if next <= 100:
            if next in good:
                next = good[next]
            if next in bad:
                next = bad[next]
            if not visited[next]:
                q.append((next, cnt+1))
                visited[next] = True