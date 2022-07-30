import sys
input = sys.stdin.readline
size = int(input())
matrix = []

def solution(i, j, size) :
    check = matrix[i][j]
    new_size = size//2
    for k in range(i, i + size) :
        for z in range(j, j + size) :
            if check != matrix[k][z] :
                print("(", end = "")
                solution(i, j, new_size)
                solution(i, j+new_size, new_size)
                solution(i+new_size, j, new_size)
                solution(i + new_size, j + new_size, new_size)
                print(")", end ="")
                return
    if check == 0 :
        print('0', end = "")
        return
    else :
        print('1', end = "")
        return
for i in range(size) :
    tmp = input()
    tmp_matrix = []
    for j in range(size) :
        tmp_matrix.append(int(tmp[j]))
    matrix.append(tmp_matrix)
solution(0, 0, size)