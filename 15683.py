from copy import deepcopy

n, m = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(n)]
direction = [[],[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]
cctv = []
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i,j,office[i][j]])

def update(graph,x,y):
    if graph[x][y] == 0:
        graph[x][y] = '#'
    elif graph[x][y] == 6:
        return False
    return True

def surveillance(graph,X,Y,dir):
    for d in dir:
        x = X
        y = Y
        if d == 0:
            while x>=0:
                if not update(graph,x,y):
                    break
                x -= 1
        elif d == 1:
            while y<m:
                if not update(graph,x,y):
                    break
                y += 1
        elif d == 2:
            while x<n:
                if not update(graph,x,y):
                    break
                x += 1
        elif d == 3:
            while y>=0:
                if not update(graph,x,y):
                    break
                y -= 1

def dfs(graph, depth):
    if depth == len(cctv):
        global answer
        cnt = 0
        for g in graph:
            cnt += g.count(0)
        answer = min(answer, cnt)
        return

    graph_cp = deepcopy(graph)
    x, y, type = cctv[depth]
    for dir in direction[type]:
        surveillance(graph_cp, x, y, dir)
        dfs(graph_cp,depth+1)
        graph_cp = deepcopy(graph)

answer = m*n
dfs(office,0)
print(answer)