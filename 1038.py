import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
d = ['0','1','2','3','4','5','6','7','8','9']
dec = []
for i in range(1,11):
    for c in combinations(d,i):
        c = list(c)
        c.sort(reverse=True)
        tmp = ""
        for cc in c:
            tmp += cc
        dec.append(int(tmp))
dec.sort()
if n < len(dec):
    print(dec[n])
else:
    print(-1)