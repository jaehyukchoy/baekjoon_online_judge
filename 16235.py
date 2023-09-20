import math
import sys
from copy import deepcopy
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
s2d2 = [[5] * (n + 1) for _ in range(n + 1)]
a = []
land = [[deque() for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    land[x][y].append(z)
seasons = ["spring", "fall"]
d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while k > 0:
    k -= 1
    for season in seasons:
        if season == "spring":
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    s = 0
                    tmp = deque()
                    for age in land[i][j]:
                        if s2d2[i][j] >= age:
                            s2d2[i][j] -= age
                            tmp.append(age+1)
                        else:
                            s += math.floor(age / 2)
                    land[i][j] = tmp
                    s2d2[i][j] += s

        elif season == "fall":
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    for age in land[i][j]:
                        if age % 5 == 0:
                            for dx, dy in d:
                                nx = i + dx
                                ny = j + dy
                                if 0 < nx <= n and 0 < ny <= n:
                                    land[nx][ny].appendleft(1)
                    s2d2[i][j] += a[i - 1][j - 1]


answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        answer += len(land[i][j])
print(answer)
