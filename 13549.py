from collections import deque

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
        flag = True
        if i == 0:
            nx = x - 1
        elif i == 1:
            nx = x + 1
        else:
            nx = x * 2
            flag = False
        if 0 <= nx <= 200000:
            if not v[nx]:
                v[nx] = True
                d[nx] = d[x] + 1 if flag else d[x]
                q.append(nx)
            elif d[nx] > d[x]:
                d[nx] = d[x] + 1 if flag else d[x]
