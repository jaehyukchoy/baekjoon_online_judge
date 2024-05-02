k = 0
while True:
    k += 1
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    graph[0][0] = 1000
    graph[0][2] += graph[0][1]
    for i in range(1, n):
        graph[i][0] += min(graph[i - 1][0], graph[i - 1][1])
        graph[i][1] += min(
            graph[i][0], graph[i - 1][0], graph[i - 1][1], graph[i - 1][2]
        )
        graph[i][2] += min(graph[i][1], graph[i - 1][1], graph[i - 1][2])
    print(k, graph[n - 1][1], sep=". ")
