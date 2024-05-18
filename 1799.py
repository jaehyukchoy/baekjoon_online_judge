from collections import deque


def find(x, y, q):
    ret = deque()
    for nx, ny in q:
        if x != nx:
            a = (ny - y) / (nx - x)
            if a == 1 or a == -1:
                continue
        ret.append((nx, ny))
    return ret


def solve(q, cnt):
    global ans
    ans = max(ans, cnt)
    while q:
        x, y = q.popleft()
        solve(find(x, y, q), cnt + 1)


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

q1 = deque()
q2 = deque()
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            if (i + j) % 2 == 0:
                q1.append((i, j))
            else:
                q2.append((i, j))

answer = 0
ans = 0
solve(q1, 0)
answer += ans
ans = 0
solve(q2, 0)
answer += ans
print(answer)
