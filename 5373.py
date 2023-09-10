reps=[]
rot=[]
for _ in range(int(input())):
    reps.append(int(input()))
    rot.append(list(input().split()))

while reps:
    _reps=reps.pop(0)
    _rot=rot.pop(0)
    cube = [['.','.','.','o','o','o','.','.','.','.','.','.'],
            ['.','.','.','o','o','o','.','.','.','.','.','.'],
            ['.','.','.','o','o','o','.','.','.','.','.','.'],
            ['g','g','g','w','w','w','b','b','b','y','y','y'],
            ['g','g','g','w','w','w','b','b','b','y','y','y'],
            ['g','g','g','w','w','w','b','b','b','y','y','y'],
            ['.','.','.','r','r','r','.','.','.','.','.','.'],
            ['.','.','.','r','r','r','.','.','.','.','.','.'],
            ['.','.','.','r','r','r','.','.','.','.','.','.']]  

    for r in _rot:
        if r == 'L-':
            tmp = [cube[0][3],cube[1][3],cube[2][3]]
            for i in range(6):
                cube[i][3] = cube[i+3][3]
            for i in range(6,9):
                cube[i][3] = cube[11-i][11]
                cube[11-i][11] = tmp.pop(0)
            c1 = cube[3][0]
            c2 = cube[3][1]
            cube[3][0] = cube[3][2]
            cube[3][1] = cube[4][2]
            cube[3][2] = cube[5][2]
            cube[4][2] = cube[5][1]
            cube[5][2] = cube[5][0]
            cube[5][1] = cube[4][0]
            cube[5][0] = c1
            cube[4][0] = c2
        elif r == 'L+':
            tmp = [cube[8][3],cube[7][3],cube[6][3]]
            for i in range(8,2,-1):
                cube[i][3] = cube[i-3][3]
            for i in range(2,-1,-1):
                cube[i][3] = cube[5-i][11]
                cube[5-i][11] = tmp.pop(0)
            c1 = cube[3][0]
            c2 = cube[4][0]
            cube[3][0] = cube[5][0]
            cube[4][0] = cube[5][1]
            cube[5][0] = cube[5][2]
            cube[5][1] = cube[4][2]
            cube[5][2] = cube[3][2]
            cube[4][2] = cube[3][1]
            cube[3][2] = c1
            cube[3][1] = c2
            
        elif r == 'R-':
            tmp = [cube[8][5],cube[7][5],cube[6][5]]
            for i in range(8,2,-1):
                cube[i][5] = cube[i-3][5]
            for i in range(2,-1,-1):
                cube[i][5] = cube[5-i][9]
                cube[5-i][9] = tmp.pop(0)
            c1 = cube[3][6]
            c2 = cube[3][7]
            cube[3][6] = cube[3][8]
            cube[3][7] = cube[4][8]
            cube[3][8] = cube[5][8]
            cube[4][8] = cube[5][7]
            cube[5][8] = cube[5][6]
            cube[5][7] = cube[4][6]
            cube[5][6] = c1
            cube[4][6] = c2
        elif r == 'R+':
            tmp = [cube[0][5],cube[1][5],cube[2][5]]
            for i in range(6):
                cube[i][5] = cube[i+3][5]
            for i in range(6,9):
                cube[i][5] = cube[11-i][9]
                cube[11-i][9] = tmp.pop(0)
            c1 = cube[3][6]
            c2 = cube[4][6]
            cube[3][6] = cube[5][6]
            cube[4][6] = cube[5][7]
            cube[5][6] = cube[5][8]
            cube[5][7] = cube[4][8]
            cube[5][8] = cube[3][8]
            cube[4][8] = cube[3][7]
            cube[3][8] = c1
            cube[3][7] = c2      
        elif r == 'U+':
            c1 = cube[3][3]
            c2 = cube[4][3]
            cube[3][3] = cube[5][3]
            cube[4][3] = cube[5][4]
            cube[5][3] = cube[5][5]
            cube[5][4] = cube[4][5]
            cube[5][5] = cube[3][5]
            cube[4][5] = cube[3][4]
            cube[3][5] = c1
            cube[3][4] = c2
            d1 = cube[2][3]
            d2 = cube[3][2]
            d3 = cube[4][2]
            cube[2][3] = cube[5][2]
            cube[3][2] = cube[6][3]
            cube[4][2] = cube[6][4]
            cube[5][2] = cube[6][5]
            cube[6][3] = cube[5][6]
            cube[6][4] = cube[4][6]
            cube[6][5] = cube[3][6]
            cube[5][6] = cube[2][5]
            cube[4][6] = cube[2][4]
            cube[3][6] = d1
            cube[2][5] = d2
            cube[2][4] = d3
        elif r == 'U-':
            c1 = cube[3][3]
            c2 = cube[3][4]
            cube[3][3] = cube[3][5]
            cube[3][4] = cube[4][5]
            cube[3][5] = cube[5][5]
            cube[4][5] = cube[5][4]
            cube[5][5] = cube[5][3]
            cube[5][4] = cube[4][3]
            cube[5][3] = c1
            cube[4][3] = c2
            d1 = cube[2][3]
            d2 = cube[2][4]
            d3 = cube[2][5]
            cube[2][3] = cube[3][6]
            cube[2][4] = cube[4][6]
            cube[2][5] = cube[5][6]
            cube[3][6] = cube[6][5]
            cube[4][6] = cube[6][4]
            cube[5][6] = cube[6][3]
            cube[6][5] = cube[5][2]
            cube[6][4] = cube[4][2]
            cube[6][3] = cube[3][2]
            cube[5][2] = d1
            cube[4][2] = d2
            cube[3][2] = d3
        elif r == 'D+':
            c1 = cube[3][9]
            c2 = cube[4][9]
            cube[3][9] = cube[5][9]
            cube[4][9] = cube[5][10]
            cube[5][9] = cube[5][11]
            cube[5][10] = cube[4][11]
            cube[5][11] = cube[3][11]
            cube[4][11] = cube[3][10]
            cube[3][11] = c1
            cube[3][10] = c2
            d1 = cube[0][3]
            d2 = cube[0][4]
            d3 = cube[0][5]
            cube[0][3] = cube[3][8]
            cube[0][4] = cube[4][8]
            cube[0][5] = cube[5][8]
            cube[3][8] = cube[8][5]
            cube[4][8] = cube[8][4]
            cube[5][8] = cube[8][3]
            cube[8][5] = cube[5][0]
            cube[8][4] = cube[4][0]
            cube[8][3] = cube[3][0]
            cube[5][0] = d1
            cube[4][0] = d2
            cube[3][0] = d3
        elif r == 'D-':
            c1 = cube[3][9]
            c2 = cube[3][10]
            cube[3][9] = cube[3][11]
            cube[3][10] = cube[4][11]
            cube[3][11] = cube[5][11]
            cube[4][11] = cube[5][10]
            cube[5][11] = cube[5][9]
            cube[5][10] = cube[4][9]
            cube[5][9] = c1
            cube[4][9] = c2
            d1 = cube[0][3]
            d2 = cube[3][0]
            d3 = cube[4][0]
            cube[0][3] = cube[5][0]
            cube[3][0] = cube[8][3]
            cube[4][0] = cube[8][4]
            cube[5][0] = cube[8][5]
            cube[8][3] = cube[5][8]
            cube[8][4] = cube[4][8]
            cube[8][5] = cube[3][8]
            cube[5][8] = cube[0][5]
            cube[4][8] = cube[0][4]
            cube[3][8] = d1
            cube[0][5] = d2
            cube[0][4] = d3
        elif r == 'F+':
            tmp = [cube[5][11],cube[5][10],cube[5][9]]
            for i in range(11,2,-1):
                cube[5][i] = cube[5][i-3]
            for i in range(2,-1,-1):
                cube[5][i] = tmp.pop(0)
            c1 = cube[6][3]
            c2 = cube[7][3]
            cube[6][3] = cube[8][3]
            cube[7][3] = cube[8][4]
            cube[8][3] = cube[8][5]
            cube[8][4] = cube[7][5]
            cube[8][5] = cube[6][5]
            cube[7][5] = cube[6][4]
            cube[6][5] = c1
            cube[6][4] = c2
        elif r == 'F-':
            tmp = [cube[5][0],cube[5][1],cube[5][2]]
            for i in range(9):
                cube[5][i] = cube[5][i+3]
            for i in range(9,12):
                cube[5][i] = tmp.pop(0)
            c1 = cube[6][3]
            c2 = cube[6][4]
            cube[6][3] = cube[6][5]
            cube[6][4] = cube[7][5]
            cube[6][5] = cube[8][5]
            cube[7][5] = cube[8][4]
            cube[8][5] = cube[8][3]
            cube[8][4] = cube[7][3]
            cube[8][3] = c1
            cube[7][3] = c2
        elif r == 'B+':
            tmp = [cube[3][0],cube[3][1],cube[3][2]]
            for i in range(9):
                cube[3][i] = cube[3][i+3]
            for i in range(9,12):
                cube[3][i] = tmp.pop(0)
            c1 = cube[0][3]
            c2 = cube[1][3]
            cube[0][3] = cube[2][3]
            cube[1][3] = cube[2][4]
            cube[2][3] = cube[2][5]
            cube[2][4] = cube[1][5]
            cube[2][5] = cube[0][5]
            cube[1][5] = cube[0][4]
            cube[0][5] = c1
            cube[0][4] = c2  
        elif r == 'B-':
            tmp = [cube[3][11],cube[3][10],cube[3][9]]
            for i in range(11,2,-1):
                cube[3][i] = cube[3][i-3]
            for i in range(2,-1,-1):
                cube[3][i] = tmp.pop(0)
            c1 = cube[0][3]
            c2 = cube[0][4]
            cube[0][3] = cube[0][5]
            cube[0][4] = cube[1][5]
            cube[0][5] = cube[2][5]
            cube[1][5] = cube[2][4]
            cube[2][5] = cube[2][3]
            cube[2][4] = cube[1][3]
            cube[2][3] = c1
            cube[1][3] = c2

    #for z in range(9):
    #    print(cube[z])

    print(cube[3][3]+cube[3][4]+cube[3][5])
    print(cube[4][3]+cube[4][4]+cube[4][5])
    print(cube[5][3]+cube[5][4]+cube[5][5])