from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
q = deque([n])
v = [False] * 200001
d = [0] * 200001
v[n] = True
d[n] = 0

while q:
    x = q.popleft()
    if x == k:
        print(d[k])
        break
    for i in range(3):
        if i == 0:
            nx = x - 1
        elif i == 1:
            nx = x + 1
        else:
            nx = x * 2
        if 0 <= nx <= 200000:
            if not v[nx]:
                v[nx] = True
                d[nx] = d[x] + 1
                q.append(nx)

p = deque([k])
q2 = deque([k])
vv = [False] * 200001
vv[k] = True


def dfs(qq, pp):
    if not qq:
        return
    xx = qq.popleft()
    if xx == n:
        for iii in range(len(pp) - 1, -1, -1):
            print(pp[iii], end=" ")
        exit()
    f = 3 if xx % 2 == 0 else 2
    for i in range(f):
        if i == 0:
            nx = xx - 1
        elif i == 1:
            nx = xx + 1
        else:
            nx = int(xx / 2)
        if 0 <= nx <= 200000 and d[nx] == d[xx] - 1:
            if not vv[nx]:
                vv[nx] = True
                qq.append(nx)
                pp.append(nx)
                dfs(qq, pp)
                pp.pop()


dfs(q2, p)
