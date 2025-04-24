from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, target):
    visited = [False] * 10000
    from_ = [-1] * 10000
    how = [''] * 10000

    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        if now == target:
            break

        d = (now * 2) % 10000
        if not visited[d]:
            visited[d] = True
            from_[d] = now
            how[d] = 'D'
            q.append(d)

        s = now - 1 if now != 0 else 9999
        if not visited[s]:
            visited[s] = True
            from_[s] = now
            how[s] = 'S'
            q.append(s)

        l = (now % 1000) * 10 + (now // 1000)
        if not visited[l]:
            visited[l] = True
            from_[l] = now
            how[l] = 'L'
            q.append(l)

        r = (now % 10) * 1000 + (now // 10)
        if not visited[r]:
            visited[r] = True
            from_[r] = now
            how[r] = 'R'
            q.append(r)

    res = []
    cur = target
    while cur != start:
        res.append(how[cur])
        cur = from_[cur]
    return ''.join(reversed(res))

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bfs(A, B))
