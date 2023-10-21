x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

def ccw(p1,q1,p2,q2,p3,q3):
    s=(p2-p1)*(q3-q1)-(q2-q1)*(p3-p1)
    if s>0:
        return 1
    elif s<0:
        return -1
    else:
        return 0

if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<0:
    print(1)
elif ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)==0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)==0:
    if min(x3,x4)<=max(x1,x2) and min(y3,y4)<=max(y1,y2) and min(x1,x2)<=max(x3,x4) and min(y1,y2)<=max(y3,y4):
        print(1)
    else:
        print(0)
elif ccw(x1,y1,x2,y2,x3,y3)==0:
    if min(x1,x2)<=x3<=max(x1,x2) and min(y1,y2)<=y3<=max(y1,y2):
        print(1)
    else:
        print(0)
elif ccw(x1,y1,x2,y2,x4,y4)==0:
    if min(x1,x2)<=x4<=max(x1,x2) and min(y1,y2)<=y4<=max(y1,y2):
        print(1)
    else:
        print(0)
elif ccw(x3,y3,x4,y4,x1,y1)==0:
    if min(x3,x4)<=x1<=max(x3,x4) and min(y3,y4)<=y1<=max(y3,y4):
        print(1)
    else:
        print(0)
elif ccw(x3,y3,x4,y4,x2,y2)==0:
    if min(x3,x4)<=x2<=max(x3,x4) and min(y3,y4)<=y2<=max(y3,y4):
        print(1)
    else:
        print(0)
else:
    print(0)