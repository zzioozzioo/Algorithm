import sys

while True:
    input = sys.stdin.readline().rstrip()
    string_list = []

    if input == '.':
        break

    for i in input:
        if input == '(' or input == '[':
            string_list.append(input)
        elif input == ')':
            if '(' in string_list and string_list[-1]=='(':
                string_list.pop()
            else: # 짝이 안 맞으면
                string_list.append(input)
                break
        elif input == ']':
            if '[' in string_list and string_list[-1]=='[':
                string_list.pop()
            else: # 짝이 안 맞으면
                string_list.append(input)
                break

    if not string_list:
        print('yes')
    else:
        print('no')