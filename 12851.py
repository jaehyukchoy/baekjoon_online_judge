from collections import deque

n, k = map(int, input().split())
q = deque([n])
v = [False] * 200001
d = [0] * 200001
c = [0] * 200001
v[n] = True
d[n] = 0
c[n] = 1
while q:
    x = q.popleft()
    if x == k:
        print(d[k])
        print(c[k])
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
                c[nx] = c[x]
                q.append(nx)
            elif d[nx] > d[x]:
                c[nx] += c[x]