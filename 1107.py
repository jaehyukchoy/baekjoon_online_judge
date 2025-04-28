import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = set(map(int, input().split())) if m else set()

ans = abs(n - 100)

for num in range(1000000):
    for ch in str(num):
        if int(ch) in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(n - num))

print(ans)
