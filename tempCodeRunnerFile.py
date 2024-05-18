def find(x, y):
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        i = 1
        nx, ny = x + i * dx, y + i * dy
        while 0 <= nx < n and 0 <= ny < n:
            if g[nx][ny] == 2:
                return True
            i += 1
            nx, ny = x + i * dx, y + i * dy
    return False


def solve(cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1 and not find(i, j):

                g[i][j] = 2
                solve(cnt + 1)
                g[i][j] = 3


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]


ans = 0
solve(0)
print(ans)
