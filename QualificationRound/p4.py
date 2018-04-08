import sys
import math

T = int(sys.stdin.readline().strip())

def sind(DEG):
    return math.sin(math.radians(DEG))
def cosd(DEG):
    return math.cos(math.radians(DEG))
def tand(DEG):
    return math.tan(math.radians(DEG))

def mul(M,V):
    R = [0 for i in V]
    for i in range(len(M)):
        for j in range(len(M[i])):
                R[i] += M[i][j] * V[j]
    return R

def rotx(DEG, V):
    M = [
        [      1.0,       0.0, 0.0],
        [0.0, math.cos(DEG),-math.sin(DEG)],
        [0.0, math.sin(DEG), math.cos(DEG)],
        ]
    return mul(M, V)

def rotz(DEG, V):
    M = [
        [math.cos(DEG),-math.sin(DEG), 0.0],
        [math.sin(DEG), math.cos(DEG), 0.0],
        [      0.0,       0.0, 1.0],
        ]
    return mul(M, V)

SQ2 = math.sqrt(2.0)
SQ3 = math.sqrt(3.0)

def printv(V):
    print(" ".join([str(i) for i in V]))

def CALC(T):
    Z = 0.0
    X = 0.0
    if T <= SQ2:
        Z = math.asin(T/SQ2) - math.radians(45.0)
    else:
        Z = math.radians(45.0)
        X = math.radians(45.0) - math.acos(T/(SQ2 * 2 * sind(45.0)))
    Z = round(Z, 10)
    X = round(X, 10)
    printv(rotx(X, rotz(Z, [0.5, 0.0, 0.0])))
    printv(rotx(X, rotz(Z, [0.0, 0.5, 0.0])))
    printv(rotx(X, rotz(Z, [0.0, 0.0, 0.5])))

def ab(V):
    return sum([i * i for i in V])

for times in range(T):
    A = float(sys.stdin.readline().strip())
    print("Case #{}:".format(times + 1))
    CALC(A)
exit(0)
