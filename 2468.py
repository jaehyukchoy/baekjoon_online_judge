from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

d = [(-1,0),(1,0),(0,1),(0,-1)]
def bfs(p, q, height, visited):
    visited[p][q] = 1
    li = deque()
    li.append((p,q))
    while li:
        x,y = li.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n:
                if b[nx][ny] > height and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    li.append((nx,ny))

if __name__ == "__main__":
    n = int(input())
    b = list(list(map(int,input().split())) for _ in range(n))
    answer = 0
    for i in range(0,101):
        visited = [[0]*n for _ in range(n)]
        r = 0
        for p in range(n):
            for q in range(n):
                if b[p][q] > i and visited[p][q] == 0:
                    bfs(p,q,i,visited)
                    r += 1
        answer = max(answer,r)
    print(answer)