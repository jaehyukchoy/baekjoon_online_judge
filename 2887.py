n = int(input())
planet = []
for idx in range(n):
    planet.append(list(map(int, input().split())) + [idx])

ex = []
planet.sort(key=lambda k: k[0])
for i in range(n - 1):
    xa, ya, za, a = planet[i]
    xb, yb, zb, b = planet[i + 1]
    ex.append((abs(xa - xb), a, b))

ey = []
planet.sort(key=lambda k: k[1])
for i in range(n - 1):
    xa, ya, za, a = planet[i]
    xb, yb, zb, b = planet[i + 1]
    ey.append((abs(ya - yb), a, b))

ez = []
planet.sort(key=lambda k: k[2])
for i in range(n - 1):
    xa, ya, za, a = planet[i]
    xb, yb, zb, b = planet[i + 1]
    ez.append((abs(za - zb), a, b))

edges = ex + ey + ez
edges.sort()

parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


result = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)
