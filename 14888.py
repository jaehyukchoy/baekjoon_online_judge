import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxVal = -sys.maxsize
minVal = sys.maxsize

def dfs(val, i, a, s, m, d):
    global maxVal
    global minVal
    if i == n:
        maxVal = max(maxVal, val)
        minVal = min(minVal, val)
        return

    if a > 0:
        dfs(val + num[i], i + 1, a - 1, s, m, d)
    if s > 0:
        dfs(val - num[i], i + 1, a, s - 1, m, d)
    if m > 0:
        dfs(val * num[i], i + 1, a, s, m - 1, d)
    if d > 0:
        if val >= 0:
            dfs(val // num[i], i + 1, a, s, m, d - 1)
        else:
            dfs(-((-val) // num[i]), i + 1, a, s, m, d - 1)
        
dfs(num[0], 1, add, sub, mul, div)
print(maxVal)
print(minVal)