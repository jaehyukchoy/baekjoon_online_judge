from collections import deque

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

arr = deque([])
def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(n):
        if not visited[i]:
            arr.append(num[i])
            visited[i] = True
            dfs()
            arr.pop()
            visited[i] = False

visited = [False] * n
dfs()