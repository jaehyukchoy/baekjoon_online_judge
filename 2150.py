from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def kosaraju(n, graph, reversed):
    visited = [False] * (n+1)
    s = []
    def dfs(node):
        visited[node] = True
        for next in graph[node]:
            if not visited[next]:
                dfs(next)
        s.append(node)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    
    visited = [False] * (n+1)
    sccs = []
    def dfs2(node, scc):
        visited[node] = True
        scc.append(node)
        for next in reversed[node]:
            if not visited[next]:
                dfs2(next, scc)

    while s:
        node = s.pop()
        if not visited[node]:
            scc = []
            dfs2(node, scc)
            scc.sort()
            scc.append(-1)
            sccs.append(scc)
    sccs.sort(key=lambda x:x[0])
    return sccs

v, e = map(int, input().split())
graph = defaultdict(list)
reversed = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    reversed[b].append(a)
sccs = kosaraju(v, graph, reversed)
print(len(sccs))
for scc in sccs:
    print(' '.join(map(str, scc)))