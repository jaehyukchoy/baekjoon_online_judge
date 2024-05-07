from collections import deque

n = int(input())
g = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
for i in range(1, n + 1):
    t, m, *mm = list(map(int, input().split()))
    time[i] = t
    for mmm in mm:
        g[i].append(mmm)

for i in range(1, n + 1):
    tmp = 0
    for j in g[i]:
        tmp = max(tmp, time[j])
    time[i] += tmp

print(max(time))
