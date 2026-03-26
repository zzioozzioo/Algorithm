import sys
input = sys.stdin.readline

import heapq
heap = []

N = int(input())
for _ in range(N):
    data = int(input())

    if data == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    
    else:
        heapq.heappush(heap, -data)