def mul(ma, mb):
    n = len(ma)
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += ma[i][k] * mb[k][j]
            m[i][j] = tmp % 1000000007
    return m


def pow(m, b):
    n = len(m)
    if b == 1:
        new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new[i][j] = m[i][j] % 1000000007
        return new
    mm = pow(m, b // 2)
    if b % 2 == 0:
        return mul(mm, mm)
    else:
        return mul(mul(mm, mm), m)


d = int(input())
matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

ans = pow(matrix, d)
print(ans[0][0])
