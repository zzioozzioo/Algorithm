import sys
from collections import deque

input = sys.stdin.readline

N = int(sys.stdin.readline().rstrip())
deq = deque(map(int, sys.stdin.readline().rstrip().split()))

index = 0
for i in range(N):
    index = index % len(deq)
    index = deq.pop(deq[index])
    if index > 0:
        index = deq.pop(deq[index-1])
    else:
        index = deq.pop(deq[index])