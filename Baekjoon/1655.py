import sys
import heapq

input = sys.stdin.readline
N = int(input())
max_heap = []
min_heap = []

field = []
for _ in range(N) :
    num = int(input())
    if len(max_heap) == len(min_heap) :
        heapq.heappush(max_heap, -num)
    else :
        heapq.heappush(min_heap, num)
    if min_heap and -max_heap[0] > min_heap[0] :
        A = heapq.heappop(max_heap)
        B = heapq.heappop(min_heap)
        heapq.heappush(min_heap, -A)
        heapq.heappush(max_heap, -B)
    print(-max_heap[0])