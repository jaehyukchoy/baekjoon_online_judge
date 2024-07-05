n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
ans = []


def dfs(now):
    if len(arr) == m:
        ans.append(arr[:])
        return

    for i in range(now, n):
        arr.append(num[i])
        dfs(i)
        arr.pop()


dfs(0)

for a in sorted(list(set(map(tuple, ans)))):
    print(" ".join(map(str, a)))
