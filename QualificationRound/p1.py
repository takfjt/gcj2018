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
