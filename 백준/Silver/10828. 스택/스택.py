import sys
input = sys.stdin.readline

N = int(input())

stack = []
top = -1

for _ in range(N):
    op = input().split() # op[0], op[1]

    if op[0] == 'push':
        data = int(op[1])
        stack.append(data)
        top += 1
        # print(stack)

    elif op[0] == 'pop': 
        if top >= 0: # 비어있지 않으면 데이터 가져오고
            top -= 1
            print(stack.pop())
        else: # 비어있으면 -1
            print(-1)

    elif op[0] == 'size':
        print(top+1)

    elif op[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)

    elif op[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])