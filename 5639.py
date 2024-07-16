import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(left, right):
    if left>right:
        return
    mid = right+1
    for i in range(left+1, right+1):
        if tree[i]>tree[left]:
            mid = i
            break
    postorder(left+1, mid-1)
    postorder(mid,right)
    print(tree[left])

postorder(0, len(tree)-1)