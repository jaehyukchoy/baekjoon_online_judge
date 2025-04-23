import sys
input = sys.stdin.readline

class KthSegmentTree:
    def __init__(self, MAX=2_000_000_000):
        self.tree = {}
        self.MAX = MAX

    def update(self, node, l, r, idx, diff):
        if idx < l or idx > r:
            return
        self.tree[node] = self.tree.get(node, 0) + diff
        if self.tree[node] == 0:
            del self.tree[node]
        if l == r:
            return
        mid = (l + r) // 2
        self.update(node*2, l, mid, idx, diff)
        self.update(node*2+1, mid+1, r, idx, diff)

    def kth(self, node, l, r, k):
        if l == r:
            return l
        mid = (l + r) // 2
        left_count = self.tree.get(node*2, 0)
        if k <= left_count:
            return self.kth(node*2, l, mid, k)
        else:
            return self.kth(node*2+1, mid+1, r, k - left_count)


tree = KthSegmentTree()

for _ in range(int(input())):
    ipt = list(map(int, input().split()))
    if ipt[0] == 1:
        kth_val = tree.kth(1, 1, tree.MAX, ipt[1])
        print(kth_val)
        tree.update(1, 1, tree.MAX, kth_val, -1)
    else:
        tree.update(1, 1, tree.MAX, ipt[1], ipt[2])
