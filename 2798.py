import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int,input().split())
num = list(map(int,input().split()))
answer = 0
for c in combinations(num, 3):
    s = sum(c)
    if s <= m and answer < s:
        answer = s
print(answer)