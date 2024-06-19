import math
a, b = map(int, input().split())

def solve(n):
    if n <= 0:
        return 0
    l = int(math.log2(n))
    diff = n-2**l
    if diff == 0:
        return int(1+l*(2**(l-1)))
    else:
        return solve(2**l)+solve(diff)+diff

print(solve(b) - solve(a-1))