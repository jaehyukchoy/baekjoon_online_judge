import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
num = []
for _ in range(n):
    num.append(int(input()))

tree = [0] * (4 * n)

def make_tree(start, end, node):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = make_tree(start, mid, node * 2) + make_tree(mid + 1, end, node * 2 + 1)
    return tree[node]
make_tree(0, n - 1, 1)

def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)

def update(start, end, node, idx, val):
    if start <= idx <= end:
        tree[node] += val
        if start < end:
            mid = (start + end) // 2
            update(start, mid, node * 2, idx, val)
            update(mid + 1, end, node * 2 + 1, idx, val)
    
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n - 1, 1, b - 1, c - num[b - 1])
        num[b - 1] = c
    else:
        print(query(0, n - 1, 1, b - 1, c - 1))
