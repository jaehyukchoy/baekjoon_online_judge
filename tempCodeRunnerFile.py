)] * (n+1)
    d[start] = 0
    for i in range(n):
        for s, e, t in edges:
            if d[s] != float('inf') and d[e] > d[s] + t:
                d[e] = d[s] + t
                if i == n-1 and e == start:
                    return True
    if d[start] < 0:
        return True
    else:
        return False