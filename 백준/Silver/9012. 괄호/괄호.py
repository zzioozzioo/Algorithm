import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    string_list = []
    input = sys.stdin.readline().strip()
    
    for j in input:
        if j == '(':
            string_list.append(j)
        elif j == ')':
            if string_list: # 리스트가 비어있지 않은 경우
                string_list.pop() # 가장 마지막으로 append한 '('를 삭제
            else: # 리스트가 비어있는 경우
                string_list.append(j)
                break
    if not string_list: # 리스트가 비어있는 경우
        print('YES')
    else:
        print('NO') # 리스트가 비어있지 않고 (짝이 맞지 않은) 괄호가 남아있는 경우

