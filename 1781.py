import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0],-x[1]))

ans = 0
s = 0
q = []
for t, v in arr:
    if t > s:
        ans += v
        heapq.heappush(q, v)
        s += 1
    else:
        if q:
            mv = heapq.heappop(q)
            if mv < v:
                ans += v - mv
                heapq.heappush(q, v)
            else:
                heapq.heappush(q, mv)
print(ans)
