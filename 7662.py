import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    visited = [False] * 1000001

    for i in range(k):
        cmd, val = input().split()
        val = int(val)

        if cmd == "I":
            heapq.heappush(min_h, (val, i))
            heapq.heappush(max_h, (-val, i))
            visited[i] = True

        else:
            if val == 1:
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)

            else:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)

    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])
