for _ in range(int(input())):
    n = int(input())
    price = list(map(int, input().split()))
    ans = 0
    ma = [0] * n
    m = 0
    for i in range(n - 1, -1, -1):
        if m < price[i]:
            m = price[i]
            ma[i] = price[i]
        else:
            ma[i] = m

    for i in range(n - 1):
        ans += max(0, ma[i + 1] - price[i])
    print(ans)
