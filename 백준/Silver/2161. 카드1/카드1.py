import sys
input = sys.stdin.readline

from collections import deque
queue = deque()

N = int(input())
for i in range(1, N+1): # 카드 세팅
    queue.append(i)

while len(queue) > 1: # 카드가 한 장 남을 때까지 반복
    print(queue.popleft(), end=' ') # 맨 위에 있는 카드 버리기
    queue.append(queue.popleft()) # 맨 위에 있는 카드->가장 아래로 옮기기

print(queue.pop())