N = int(input())
row = [0] * N

def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i]-row[x]) == x-i:
            return False
    return True

def solve(x):
    global ans
    if x == N:
        ans += 1
        return
    
    for i in range(N):
        row[x] = i
        if check(x):
            solve(x+1)


ans = 0
solve(0)
print(ans)