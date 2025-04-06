import math
import sys
input = sys.stdin.readline

MOD = 1_000_000_007
n, m, k = map(int, input().split())
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [1] * tree_size
arr = [int(input()) for _ in range(n)]

def build():
    for i in range(n):
        tree[i + tree_size // 2] = arr[i]

    for i in range(tree_size // 2 - 1, 0, -1):
        left, right = tree[i * 2], tree[i * 2 + 1]
        tree[i] = left * right % MOD

build()

def update(idx, new):
    idx += tree_size // 2
    tree[idx] = new
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % MOD


def query(l, r):
    l += tree_size // 2
    r += tree_size // 2
    ret = 1

    while l <= r:
        if l % 2 == 1:
            ret *= tree[l] % MOD
            l += 1
        if r % 2 == 0:
            ret *= tree[r] % MOD
            r -= 1
        l //= 2
        r //= 2

    return ret


for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a==1:
        update(b-1, c)
    else:
        print(query(b-1, c-1)%MOD)