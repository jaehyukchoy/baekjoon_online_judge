import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, n-1
best_sum = float('inf')
ans_l, ans_r = 0, 0

while l < r:
    s = arr[l] + arr[r]
    if abs(s) < best_sum:
        best_sum = abs(s)
        ans_l, ans_r = arr[l], arr[r]
    
    if s == 0:
        break
    elif s < 0:
        l += 1
    else:
        r -= 1

print(ans_l, ans_r)
