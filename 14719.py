import sys
input = sys.stdin.readline
h, w = map(int,input().split())
b = [[0] * w for _ in range(h)]
block = list(map(int,input().split()))
for ww in range(w):
    for hh in range(block[ww]):
        b[hh][ww] = 1

answer = 0
for hh in range(h):
    wall = False
    tmp = 0
    for ww in range(w):
        if not wall and b[hh][ww] == 1:
            wall = True
        elif wall and b[hh][ww] == 0:
            tmp += 1
        elif wall and b[hh][ww] == 1:
            answer += tmp
            tmp = 0
print(answer)