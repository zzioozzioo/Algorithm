import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
queue = deque()

for i in range(N):
    line = sys.stdin.readline().rstrip().split()

    if line[0] == 'push':
        queue.append(int(line[1]))
    elif line[0] == 'pop':
        if queue:
           print(queue.popleft())
        else:
            print(-1) 
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
