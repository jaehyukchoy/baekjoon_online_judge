n = int(input())

from collections import defaultdict

f = defaultdict(int)
f[1] = 1
f[2] = 1

def fibonacci(num):
    if f[num]:
        return f[num]
    if num % 2 == 0:
        n1 = fibonacci(num//2 - 1)
        n2 = fibonacci(num//2)
        f[num] = ((2 * n1 + n2) * n2) % 1000000007
    else:
        n1 = fibonacci((num+1)//2 - 1)
        n2 = fibonacci((num+1)//2)
        f[num] = (n1**2 + n2**2) % 1000000007
    return f[num]

print(fibonacci(n))
