import sys
input = sys.stdin.readline
T = int(input()) # 입력 데이터 수

for i in range(T):
    stack = []
    bracket = input()
    
    for j in bracket: # 하나의 테스트 데이터 검사
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택 빈 경우
                stack.append(j)
                break
            
    if not stack:
        print("YES")
    else:
        print("NO")
