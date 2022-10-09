import sys
input = sys.stdin.readline

s1 = {}
n = int(input())
for i in range(n) :
    tmp = input().strip()
    if tmp in s1 :
        s1[tmp] += 1
        print(tmp + str(s1[tmp]))
    else :
        s1[tmp] = 0
        print("OK")
