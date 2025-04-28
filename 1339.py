import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
weight = defaultdict(int)

for _ in range(n):
    word = input().strip()
    l = len(word)
    for i, ch in enumerate(word):
        weight[ch] += 10 ** (l-i-1)


sorted_weight = sorted(weight.items(), key=lambda x: -x[1])

t = dict()
top = 9
for ch, _ in sorted_weight:
    t[ch] = top
    top -= 1

ans = 0
for ch, w in weight.items():
    ans += w * t[ch]

print(ans)
