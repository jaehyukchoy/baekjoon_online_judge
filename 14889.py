import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
for c in combinations(range(n), n//2):
    d = set(range(n)) - set(c)
    s1 = 0
    s2 = 0
    for cx,cy in combinations(c, 2):
        s1 = s1 + s[cx][cy] + s[cy][cx]
    for dx,dy in combinations(d, 2):
        s2 = s2 + s[dx][dy] + s[dy][dx]
    answer = min(answer,abs(s1-s2))
print(answer)