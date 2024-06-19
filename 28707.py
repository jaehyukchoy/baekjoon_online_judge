import heapq

class Node:
    def __init__(self, arr, cost):
        self.arr = arr
        self.cost = cost
        self.visited = False
    def __lt__(self, other):
        return self.cost < other.cost
    
n = int(input())
a = list(map(int, input().split()))
m = int(input())
manipulate = [list(map(int, input().split())) for _ in range(m)]
g = dict()

def dijkstra(start):
    q = []
    heapq.heappush(q, (start.cost, start))
    
    while q:
        cost, node = heapq.heappop(q)
        if node.visited:
            continue
        node.visited = True

        for l, r, c in manipulate:
            new_arr = node.arr[:]
            new_arr[l-1], new_arr[r-1] = new_arr[r-1], new_arr[l-1]

            key = tuple(new_arr)
            if key not in g:
                new_node = Node(new_arr, cost + c)
                g[key] = new_node
                heapq.heappush(q, (g[key].cost, g[key]))
            elif cost + c < g[key].cost:
                g[key].cost = cost + c
                heapq.heappush(q, (g[key].cost, g[key]))

        

root = Node(a,0)
g[tuple(a)] = root
dijkstra(root)

target = tuple(sorted(a))

if target in g:
    print(g[target].cost)
else:
    print(-1)