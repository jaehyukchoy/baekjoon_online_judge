import itertools
import math

if __name__ == "__main__":
    answer = math.inf
    n, m = map(int, input().split())
    city = list(list(map(int,input().split())) for _ in range(n))
    house = []
    chicken = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house.append((i,j))
            elif city[i][j] == 2:
                chicken.append((i,j))
    for c in itertools.combinations(chicken,m):
        tmp = 0
        for h1,h2 in house:
            d = math.inf
            for c1,c2 in c:
                d = min(d,abs(c1-h1)+abs(c2-h2))
            tmp += d
        answer = min(answer, tmp)
    print(answer)
    
