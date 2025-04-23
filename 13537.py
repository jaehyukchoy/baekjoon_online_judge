from bisect import bisect_right
import sys
input = sys.stdin.readline

class MergeSortTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[] for _ in range(self.n * 4)]
        self.build(1, 0, self.n - 1, arr)

    def build(self, node, l, r, arr):
        if l == r:
            self.tree[node] = [arr[l]]
        else:
            mid = (l + r) // 2
            self.build(node*2, l, mid, arr)
            self.build(node*2+1, mid+1, r, arr)
            self.tree[node] = sorted(self.tree[node*2] + self.tree[node*2+1])

    def count(self, node, l, r, ql, qr, x):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            arr = self.tree[node]
            idx = bisect_right(arr, x)
            return len(arr) - idx
        mid = (l + r) // 2
        return self.count(node*2, l, mid, ql, qr, x) + self.count(node*2+1, mid+1, r, ql, qr, x)


n = int(input())
arr = list(map(int, input().split()))
mst = MergeSortTree(arr)
for _ in range(int(input())):
    i, j, k = map(int, input().split())
    print(mst.count(1, 0, n-1, i-1, j-1, k))