import sys
input = sys.stdin.readline

N = int(input())

maxi = [0, 0, 0]
mini = [0, 0, 0]
for _ in range(N):
    a, b, c = map(int, input().split())
    x, y, z = maxi
    maxi[0] = max(x, y) + a
    maxi[1] = max(x, y, z) + b
    maxi[2] = max(y, z) + c
    p, q, r = mini
    mini[0] = min(p, q) + a
    mini[1] = min(p, q, r) + b
    mini[2] = min(q, r) + c

print(max(maxi), min(mini))