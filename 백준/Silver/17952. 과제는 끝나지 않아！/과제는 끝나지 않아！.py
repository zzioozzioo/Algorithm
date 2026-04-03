import sys
input = sys.stdin.readline

N = int(input()) # 이번 학기가 몇 분인지

stack = []
sum = 0
for _ in range(N):
    hwInfo = list(map(int, input().split())) # [1, 100, 3]

    # 새로운 과제가 주어짐
    if hwInfo[0] == 1:
        stack.append(hwInfo[1])
        stack.append(hwInfo[2]-1)

    # 새로운 과제가 주어지지 않음
    elif stack and hwInfo[0] == 0:
        stack[-1] -= 1

    if stack and stack[-1] == 0: # 과제 끝(0분 남음)
            stack.pop()
            sum += stack.pop()


print(sum)
