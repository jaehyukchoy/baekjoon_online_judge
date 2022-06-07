from collections import deque
gear=[deque(map(int,list(input()))) for _ in range(4)]

def rotate(gr,d):
    if d==1:
        gr.appendleft(gr.pop())
    else:
        gr.append(gr.popleft())



for _ in range(int(input())):
    g,d=map(int,input().split())
    c=[gear[i][2]!=gear[i+1][6] for i in range(3)]
    if g==1:
        rotate(gear[0],d)
        if c[0]:
            rotate(gear[1],-d)
            if c[1]:
                rotate(gear[2],d)
                if c[2]:
                    rotate(gear[3],-d)
    elif g==2:
        rotate(gear[1],d)
        if c[0]:
            rotate(gear[0],-d)
        if c[1]:
            rotate(gear[2],-d)
            if c[2]:
                rotate(gear[3],d)

    elif g==3:
        rotate(gear[2],d)
        if c[1]:
            rotate(gear[1],-d)
            if c[0]:
                rotate(gear[0],d)
        if c[2]:
            rotate(gear[3],-d)
        
    else:
        rotate(gear[3],d)
        if c[2]:
            rotate(gear[2],-d)
            if c[1]:
                rotate(gear[1],d)
                if c[0]:
                    rotate(gear[0],-d)

print(gear[0][0]+gear[1][0]*2+gear[2][0]*4+gear[3][0]*8)