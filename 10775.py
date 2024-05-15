g = int(input())
p = int(input())
gate = [False] * (g + 1)
ans = 0
cur_max = [i for i in range(g + 1)]


for _ in range(p):
    gi = int(input())
    flag = False
    for i in range(cur_max[gi], 0, -1):
        if not gate[i]:
            ans += 1
            flag = True
            gate[i] = True
            cur_max[gi] = i - 1
            break
    if not flag:
        break
print(ans)
