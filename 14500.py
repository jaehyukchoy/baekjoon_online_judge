import sys
input = sys.stdin.readline
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0 for _ in range(m)] for _ in range(n)]
maxVal = max(map(max,paper))
answer = 0

def dfs(x, y, depth, sum):
    global answer
    if depth == 4:
        answer = max(sum, answer)
        return

    if sum + maxVal * (4 - depth) < answer:
        return

    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, depth+1, sum + paper[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, sum + paper[nx][ny])
            visited[nx][ny] = False


for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, 1, paper[x][y])
        visited[x][y] = False

print(answer)