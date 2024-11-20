import sys

while True:
    a = sys.stdin.readline().rstrip()
    string_list = []

    if a == '.':
        break

    for i in a:
        if i == '(' or i == '[':
            string_list.append(i)
        elif i == ')':
            if '(' in string_list and string_list[-1]=='(':
                string_list.pop()
            else: # 짝이 안 맞으면
                string_list.append(i)
                break
        elif i == ']':
            if '[' in string_list and string_list[-1]=='[':
                string_list.pop()
            else: # 짝이 안 맞으면
                string_list.append(i)
                break

    if not string_list:
        print('yes')
    else:
        print('no')