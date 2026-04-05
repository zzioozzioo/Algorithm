import sys
input = sys.stdin.readline

from collections import deque
queue = deque()

N = int(input())

while True:
    # -1: 종료
    data = int(input())
    if data == -1:
        break

# 양의 정수: append()
    if data > 0 and len(queue) < N:
        queue.append(data)
        continue

# 0: pop()
    if data == 0:
        queue.popleft()

# 남은 패킷 출력
# print(' '.join(queue) if queue else 'empty')
print(*(queue or ['empty',]))
# print(*queue if queue else ('empty',))
