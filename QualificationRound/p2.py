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
