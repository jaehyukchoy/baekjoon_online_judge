import sys

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]


def dfs(x, y, depth):
    global answer
    answer = max(answer, depth)
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and alphabet[board[nx][ny]] == 0:
            alphabet[board[nx][ny]] = 1
            dfs(nx, ny, depth + 1)
            alphabet[board[nx][ny]] = 0


alphabet = [0] * 26
alphabet[board[0][0]] = 1
answer = 1
dfs(0, 0, 1)
print(answer)
