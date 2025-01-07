def add(d, arr):
    if len(arr) == 0:
        return
    if arr[0] not in d:
        d[arr[0]] = {}
    add(d[arr[0]], arr[1:])


def dfs(d, depth):
    for dd in sorted(d.keys()):
        print('--' * depth + dd)
        dfs(d[dd], depth+1)

r = {}
for _ in range(int(input())):
    k = list(input().split())
    add(r, k[1:])

dfs(r, 0)