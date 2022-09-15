def solution(n):
    if n == 1 or n == 0 :
        return 1
    cache = [-1 for _ in range(251)]
    cache[0] = 0
    cache[1] = 1
    cache[2] = 3
    for i in range(3, n+1) :
        cache[i] = cache[i-1]+ 2 * cache[i-2]
    return cache[n]
while True :
    try :
        print(solution(int(input())))
    except :
        break