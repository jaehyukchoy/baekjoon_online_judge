import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [(float('inf'), -float('inf'))] * tree_size
arr = [int(input()) for _ in range(n)]

def build():
    for i in range(n):
        tree[i + tree_size // 2] = (arr[i], arr[i])

    for i in range(tree_size // 2 - 1, 0, -1):
        left, right = tree[i * 2], tree[i * 2 + 1]
        tree[i] = (min(left[0], right[0]), max(left[1], right[1]))

build()


def query(l, r):
    l += tree_size // 2
    r += tree_size // 2
    min_res, max_res = float('inf'), -float('inf')

    while l <= r:
        if l % 2 == 1:
            min_res = min(min_res, tree[l][0])
            max_res = max(max_res, tree[l][1])
            l += 1
        if r % 2 == 0:
            min_res = min(min_res, tree[r][0])
            max_res = max(max_res, tree[r][1])
            r -= 1
        l //= 2
        r //= 2

    return min_res, max_res

for _ in range(m):
    l, r = map(int, input().split())
    print(*query(l-1,r-1))
