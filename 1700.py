import sys
input = sys.stdin.readline
n, k = map(int,input().split())
order = list(map(int,input().split()))
use = set()
answer = 0
for idx in range(k):    
    if len(use) < n:
        use.add(order[idx])
    else:
        if order[idx] in use:
            continue
        else:
            tmp = use - set(order[idx+1:idx+n])
            i = 0
            while len(tmp) > 1 and idx+n+i < k:
                tmp.discard(order[idx+n+i])
                i += 1
            use.remove(list(tmp)[0])
            use.add(order[idx])
            answer += 1
print(answer)