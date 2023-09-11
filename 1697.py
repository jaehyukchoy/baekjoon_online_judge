from collections import deque
n, k = map(int, input().split())
q = deque([(n, 0)])
v = [False] * 200001
v[n] = True
while q:
    x, d = q.popleft()
    if x == k:
        print(d)
        break
    for i in range(3):
        if i == 0:
            nx = x - 1
        elif i == 1:
            nx = x + 1
        else:
            nx = x * 2
        if 0<=nx<=200000 and not v[nx]:
            v[nx]=True
            q.append((nx, d + 1))