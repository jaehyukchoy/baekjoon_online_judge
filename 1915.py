n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
s = []
for i in range(n - 1):
    for j in range(m - 1):
        if arr[i + 1][j + 1] > 0:
            arr[i + 1][j + 1] = min(arr[i][j], arr[i + 1][j], arr[i][j + 1]) + 1
print(max(map(max, arr)) ** 2)
