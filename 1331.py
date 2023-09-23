chess = [[False] * 6 for _ in range(6)]
answer = "Valid"
knight = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
xx = [input() for _ in range(36)]
for i, x in enumerate(xx):
    if chess[ord(x[0]) - 65][int(x[1]) - 1]:
        answer = "Invalid"
        break
    if i > 0:
        flag = False
        for kx, ky in knight:
            if ord(x[0]) + kx == ord(xx[i - 1][0]) and int(x[1]) + ky == int(
                xx[i - 1][1]
            ):
                flag = True
                break
        if not flag:
            answer = "Invalid"
            break
    chess[ord(x[0]) - 65][int(x[1]) - 1] = True
f = False
if answer == "Valid":
    for kx, ky in knight:
        if ord(xx[35][0]) + kx == ord(xx[0][0]) and int(xx[35][1]) + ky == int(
            xx[0][1]
        ):
            f = True
            break
if not f:
    answer = "Invalid"
print(answer)