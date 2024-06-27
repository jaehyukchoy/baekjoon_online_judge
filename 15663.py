n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

ans = []
arr = []
def dfs():
    if len(arr) == m:
        ans.append(arr[:])
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

for a in sorted(list(set(map(tuple, ans)))):
    print(' '.join(map(str, a)))