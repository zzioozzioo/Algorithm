N = int(input())

count = 0

for _ in range(N):
    stack = []
    word = input()
    for ch in word:

        if stack:
            item = stack.pop()
            if item != ch:
                stack.append(item)
                stack.append(ch)
                
        else:
            stack.append(ch)

    if not stack:
        count += 1

print(count)


