import math, sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tree_size = pow(2, math.ceil(math.log2(n)) + 1)
tree = [(float('inf'), -1)] * tree_size

def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], start)
    else:
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

def update(node, start, end, idx, val):
    if start == end:
        tree[node] = (val, idx)
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

def query(node, start, end, left, right):
    if right < start or end < left:
        return (float('inf'), -1)
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l = query(2 * node, start, mid, left, right)
    r = query(2 * node + 1, mid + 1, end, left, right)
    return min(l, r)

build(1, 0, n - 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, n - 1, b - 1, c)
        arr[b - 1] = c
    else:
        _, idx = query(1, 0, n - 1, b - 1, c - 1)
        print(idx + 1) 
