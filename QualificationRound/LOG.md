GCJ2018 Qualification Round 2018
----

# Saving The Universe Again

```
import sys

T = int(sys.stdin.readline().strip())

def score(L):
    s = 0
    r = 1
    for i in L:
        if i == 'C':
            r = r * 2
        elif i == 'S':
            s = s + r
    return s

def swapOne(L):
    for i in reversed(range(len(L))):
        if i == 0: break
        if L[i] == 'S' and L[i - 1] == 'C':
            L[i - 1], L[i] = L[i], L[i - 1]
            return True
    return False

for times in range(T):
    A, B = sys.stdin.readline().strip().split(' ')
    A = int(A)
    B = list(B)
    count = 0
    while True:
        s = score(B)
        if s <= A:
            print('Case #{times}: {count}'.format(times = times + 1, count = count))
            break
        if not swapOne(B):
            print('Case #{times}: IMPOSSIBLE'.format(times = times + 1))
            break
        count = count + 1


exit(0)
```

必要な操作は、CSをSCにすること。できるだけ効率高く。

ということで、後ろからCSを探してSCに変える。

今思うと、range関数の引数でやればreversed必要なかった気がする。
_Case 1_ を _Case 0_ にするお約束をやっちまって一回失敗。

# Trouble Sort

```
import sys

T = int(sys.stdin.readline().strip())
for times in range(T):
    N = int(sys.stdin.readline().strip())
    L = list(map(int, sys.stdin.readline().strip().split(' ')))
    OL = L[0::2]
    EL = L[1::2]
    OL = sorted(OL)
    EL = sorted(EL)
    RL = [None]*(len(OL) + len(EL))
    RL[0::2] = OL
    RL[1::2] = EL
    A = 'OK'
    for i in range(len(RL) - 1):
        if RL[i] > RL[i + 1]:
            A = str(i)
            break
    print(RL[0:10])
    print("Case #{t}: {a}".format(t = times + 1, a= A))
exit(0)
```

最初、先頭と末尾の矛盾を見つけようかなと思ったが、真ん中でも起こるのは当然なので、素直に奇数項偶数項をソートして元に戻してチェック。

```
RL[0::2] = OL
```

この記法ができたのでらくちん。

# Go, Gopher!

```
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
exit(0)
```

どうやら3x3を埋めながら進んでもまにあったらしいのだけど、いちおう、正方形に近い矩形を確保して、準備ができたセルからの距離を計算。いちばん距離が遠い3x3エリアを渡すようにして実行。

だいたい500回くらいでおわれてたので、まあまあだったんじゃないだろうか。

# Cubic UFO

```
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
```

Test set 1が1軸、Test set 2が2軸回さなきゃいけないことはすぐにわかったが、ANALYSISみたく斜めに回す方法をずっと考えて失敗。結局1軸を最大値まで回転。それを超えた時はもう1軸回転という方式を考えてみたが、どうやらダメだった。

なにがダメだったのか。計算がそもそも間違っていた。面積から角度への式変形を間違えた。くらいかなと思っている。
ANALYSIS見ると、binary searchとか書いてあるので、ひょっとしたら式変換じゃいけなかったのかも。ニュートン法とか使えばよかったのか

# CONCLUSION

Cubic UFOのTest set 2がクリアできなかったので79点でした。
