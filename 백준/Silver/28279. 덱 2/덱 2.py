import sys
from collections import deque

input = sys.stdin.readline

N = int(sys.stdin.readline().rstrip())

deq = deque()
for i in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))

    if line[0] == 1:
        deq.appendleft(line[1])
    elif line[0] == 2:
        deq.append(line[1])
    elif line[0] == 3:
        if deq: # 원소가 있다면
            print(deq.popleft())
        else:
            print(-1)
    elif line[0] == 4:
        if deq: # 원소가 있다면
            print(deq.pop())
        else:
            print(-1)
    elif line[0] == 5:
        print(len(deq))
    elif line[0] == 6:
        if not deq: # 원소가 없으면(비어있으면)
            print(1)
        else:
            print(0)
    elif line[0] == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif line[0] == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)
