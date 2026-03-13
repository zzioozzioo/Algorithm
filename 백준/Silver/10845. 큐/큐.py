import sys
input = sys.stdin.readline

from collections import deque
queue = deque()

N = int(input())
for _ in range(N):
    op = input().split()

    if op[0] == 'push':
        queue.append(int(op[1]))
    
    elif op[0] == 'pop':
        if queue: # 큐가 비어있지 않은 경우
            data = queue.popleft() # 앞에서 빼기
            print(data)
        else:
            print(-1)
    
    elif op[0] == 'size':
        print(len(queue))
    
    elif op[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
        # print("0" if not queue else "1")
    
    elif op[0] == 'front':
        if queue:
            print(queue[0]) # 가장 앞에 있는 데이터 index = 0
        else:
            print(-1)
    
    elif op[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)