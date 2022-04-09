from itertools import combinations
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
if k < 5:
    print(0)
else:
    alphabet = {k: v for v, k in enumerate((set(map(chr, range(ord('a'), ord('z')+1))) - {'a', 'n', 't', 'i', 'c'}))}
    answer = 0
    inpt = []
    for _ in range(n):
        tmp = 0
        for c in set(input().rstrip()) - {'a', 'n', 't', 'i', 'c'}:
            tmp |= (1 << alphabet[c])
        inpt.append(tmp)
    for c in combinations((2 ** i for i in range(21)), k - 5):
        t = sum(c)
        cnt = 0
        for i in inpt:
            if i & t == i:
                cnt += 1
        if cnt > answer:
            answer = cnt
    print(answer)