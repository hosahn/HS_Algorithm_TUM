import sys
sys.setrecursionlimit(10**6)
k = int(input())

def solution(field, visited, x, y) :
    if x >= k or y >= k :
        visited[x][y] = 0
        return 0
    if y == k - 1 and x == k-1 :
        visited[x][y] = 1
        return 1
    if visited[x][y] != -1 :
        return visited[x][y]
    jumpSize = field[x][y]
    if(solution(field, visited, x + jumpSize, y) == 1 or solution(field, visited, x, y + jumpSize) == 1) :
        visited[x][y] = 1
        return visited[x][y]
    else :
        visited[x][y] = 0
        return visited[x][y]

for i in range(k) :
    n = int(input())
    visited = [[-1 for _ in range(n)]for _ in range(n)]
    field = []
    for j in range(n) :
        tmp = list(map(int, input().split()))
        field.append(tmp)
    print(solution(field, visited, 0 ,0))
    print(visited)