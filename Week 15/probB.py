n, m = map(int, input().split())
pinetree = []
wood = []

def cross(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])

def ccw(A, B, C):
    S = cross(A,B,C)
    if S < 0: return -1
    if S == 0: return 0
    return 1

for _ in range(n):
    x, y = map(int, input().split())
    pinetree.append([x, y])
for _ in range(m):
    x, y = map(int,input().split())
    wood.append([x, y])

wood = sorted(wood, key =lambda x:x[0])
L, U = [], []
for i in wood:
    l = len(L)
    while l >= 2 and ccw(L[l - 1], L[l - 2], i) == 1:
        L.pop() 
        l = len(L)
    L.append(i)

for i in reversed(wood):
    u = len(U)
    while u >= 2 and ccw(U[u - 1], U[u - 2], i) == 1:
        U.pop()
        u = len(U)
    U.append(i)

L.pop()
U.pop()
result = L + U
result = sorted(result, key=lambda x:x[0])
for i in result:
    print(i[0], i[1], sep=' ')

