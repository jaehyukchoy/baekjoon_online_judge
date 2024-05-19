import sys

sys.setrecursionlimit(10**6)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def solve(il, ir, pl, pr):
    length = ir - il + 1
    if length < 1:
        return

    root = postorder[pr]
    print(root, "", end="")
    diff = pos[root] - il

    if diff > 0:
        solve(il, il + diff - 1, pl, pl + diff - 1)
    if diff < length - 1:
        solve(il + diff + 1, ir, pl + diff, pr - 1)


pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i
solve(0, n - 1, 0, n - 1)
