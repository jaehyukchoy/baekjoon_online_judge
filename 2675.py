for _ in range(int(input())):
    r, s = input().split()
    r = int(r)
    for ss in s:
        print(ss*r, end='')
    print()