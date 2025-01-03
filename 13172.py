import math

x = 1000000007

def helper(num, exp):
    if exp == 1:
        return num
    if exp % 2 == 0:
        tmp = helper(num, exp//2)
        return tmp * tmp % x
    else:
        tmp = helper(num, exp-1)
        return num * tmp % x


answer = 0
for _ in range(int(input())):
    n, s = map(int, input().split())
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd
    answer += s * helper(n, x-2) % x

print(answer%x)