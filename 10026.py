import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
def dfs(i,j):
    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and grid[i][j]==grid[ni][nj]:
            visited[ni][nj] = True
            dfs(ni,nj)
def dfs2(i,j):
    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<n and not visited2[ni][nj]:
            if grid[i][j]=='B' and grid[ni][nj]!='B':
                continue
            if grid[i][j]!='B' and grid[ni][nj]=='B':
                continue
            visited2[ni][nj] = True
            dfs2(ni,nj)


cnt, cnt2 = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt+=1
            visited[i][j] = True
            dfs(i,j)                
        if not visited2[i][j]:
            cnt2+=1
            visited2[i][j] = True
            dfs2(i,j)
print(cnt, cnt2)