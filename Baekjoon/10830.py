import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = map(int, input().split())


def identity(a) :
    ret = [[0 for _ in range(a)]for _ in range(a)]
    for k in range(a) :
        for z in range(a) :
            if k == z :
                ret[k][z] = 1
    return ret


def mul(U, V):
    n = len(U)
    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000
    return Z

def solution(matrix, b, ident) :
    if b == 0 :
        return ident
    if b % 2 > 0 :
        return mul(solution(matrix, b-1, ident), matrix)
    else :
        half = solution(matrix, int(b / 2), ident)
        return mul(half, half)

matrix = [[0] * a for _ in range(a)]

for i in range(a):
    tmp = list(map(int, input().split()))
    for j in range(a):
        matrix[i][j] = tmp[j]
ident = identity(a)
result = solution(matrix, b, ident)

for i in range(a) :
    for j in range(a) :
        print(result[i][j], end = " ")
    print()

