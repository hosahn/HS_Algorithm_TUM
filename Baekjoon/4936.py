import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


#vertical, horizontal, diagonal
x = [0, 0, 1, -1, 1, 1, -1, -1]
y = [1, -1, 0, 0, 1, -1, 1, -1]


def DFS(i, j) :
    visited[i][j] = 1
    for k in range(8) :
        mx = i + x[k]
        my = j + y[k]
        if mx >= 0 and mx < h and my >= 0 and my < w :
            if field[mx][my] == 1 and visited[mx][my] == 0 :
                visited[mx][my] = 1
                DFS(mx, my)
    return 1

w, h = map(int, input().split())

while w != 0 and h != 0 :
    field = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h) :
        field.append(list(map(int, input().split())))
    for i in range(h) :
        for j in range(w) :
            if field[i][j] == 1 and visited[i][j] == 0 :
                count += DFS(i,j)

    print(count)
    w, h = map(int, input().split())

