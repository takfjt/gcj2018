import sys
import math

O = 20
T = int(sys.stdin.readline().strip())


def printd(D):
    print("--",file=sys.stderr,flush=True)
    for i in D:
        print(" ".join(["{:3d}".format(j) for j in i]), file = sys.stderr, flush=True)

def distance(P, D, XR, YR):
    for x in XR:
        for y in YR:
            dist = abs(P[0] - x) + abs(P[1] - y)
            if D[x][y] > dist: D[x][y] = dist
    return D

def sumround(D, x, y):
    s = 0.0
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            s += D[i][j]
    return s

def next(D, XR, YR):
    MAX = -1
    P = None
    for x in XR:
        for y in YR:
            A = sumround(D, x, y)
            if A > MAX:
                MAX = A
                P = [x,y]
    return P



for times in range(T):
    A = int(sys.stdin.readline().strip())
    #print(times, file=sys.stderr, flush=True)
    XL = YL = int(math.sqrt(A))
    while XL * XL < A:
        XL += 1
    XR = [x for x in range(XL)]
    YR = [y for y in range(YL)]
    XR2 = XR[1:-1]
    YR2 = YR[1:-1]
    D = [[1000 for y in YR] for x in XR]
    while True:
        P = next(D, XR2, YR2)
        #print("{} {}".format(P[0],P[1]), file=sys.stderr,flush = True)
        P = [i + O for i in P]
        print("{} {}".format(P[0],P[1]), flush = True)
        XI, YI = map(int, sys.stdin.readline().strip().split(' '))
        #print(XI, YI, file=sys.stderr,flush=True)
        if XI == 0 and YI == 0: break
        if XI == -1 and YI == -1: exit(-1)
        XI -= O
        YI -= O
        #print(XI, YI, file=sys.stderr, flush=True)
        D = distance([XI, YI], D, XR, YR)
        #printd(D)
#exit(0)
