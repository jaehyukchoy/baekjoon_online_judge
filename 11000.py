import heapq
lecture = [list(map(int,input().split())) for _ in range(int(input()))]
lecture.sort(key = lambda x:x[0])
h= []
for l in lecture:
    if not h:
        heapq.heappush(h, l[1])
    else:
        if h[0] <= l[0]:
            heapq.heappop(h)
            heapq.heappush(h,l[1])
        else:
            heapq.heappush(h,l[1])
print(len(h))