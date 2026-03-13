import sys
input = sys.stdin.readline

from collections import deque
queue = deque()

N, K = map(int, input().split())
for i in range(1, N+1): # 자리 세팅
    queue.append(i)

print("<", end='')
while len(queue) > 1:
    for _ in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')

print(f'{queue[0]}>')