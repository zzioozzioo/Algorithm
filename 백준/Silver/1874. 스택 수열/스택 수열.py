def solve():

    n = int(input())
    operator = []
    stack = []

    current = 1
    for _ in range(n):
        target = int(input())

        while target >= current:
            operator.append('+') # push
            stack.append(current)
            current += 1

        if stack[-1] == target:
            operator.append('-') # pop
            stack.pop()
        else:
            print('NO')
            return
        
    operator.append('-' * len(stack))
    for operand in operator:
        print(operand)

solve()
    