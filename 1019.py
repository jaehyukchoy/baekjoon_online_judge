n = int(input())
count = [0] * 10
digit = 1

while digit <= n:
    high = n // (digit * 10)
    cur = (n // digit) % 10
    low = n % digit

    for d in range(10):
        if d != 0:
            count[d] += high * digit
        else:
            if high != 0:
                count[0] += (high - 1) * digit

        if cur > d:
            if not (d == 0 and high == 0):
                count[d] += digit
        elif cur == d:
            if not (d == 0 and high == 0):
                count[d] += low + 1

    digit *= 10

print(' '.join(map(str,count)))
