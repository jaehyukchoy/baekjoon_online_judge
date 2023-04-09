
def rotate(pivot, point):
    px, py = pivot
    x, y = point
    ny = py + (x - px)
    nx = px + (py - y)
    return (nx, ny)
    
def dragon_curve(dragon, pivot):
    new_dragon = []
    for i, point in enumerate(dragon):
        if i == 0:
            new_pivot = rotate(pivot,point)
            new_dragon.append(new_pivot)
        else:
            if point == pivot:
                continue
            new_dragon.append(rotate(pivot,point))
    return new_dragon, new_pivot

def check_square(board):
    global answer
    for i in range(100):
        for j in range(100):
            if (i,j) in board and (i+1,j) in board and (i,j+1) in board and (i+1,j+1) in board:
                answer += 1

if __name__ == "__main__":
    answer = 0
    board = []
    for j in range(int(input())):
        x, y, d, g = map(int, input().split())
        dragon = [(x,y)]
        if d == 0:
            dragon.append((x+1,y))
        elif d == 1:
            dragon.append((x,y-1))
        elif d == 2:
            dragon.append((x-1,y))
        else:
            dragon.append((x,y+1))
        pivot = dragon[-1]
        for _ in range(g):
            new_dragon, pivot = dragon_curve(dragon, pivot)
            dragon = dragon + new_dragon
        board = board + dragon
    board = list(dict.fromkeys(board))
    check_square(board)
    print(answer)
    
