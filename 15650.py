from collections import deque

n, m = map(int, input().split())

arr = deque([])
def dfs(now):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(now, n + 1):
        arr.append(i)
        dfs(i + 1)
        arr.pop()

dfs(1)