h, m = map(int, input().split())
tmp = 60 * h + m - 45
if tmp < 0:
    tmp += 24 * 60
print(tmp//60, tmp%60)