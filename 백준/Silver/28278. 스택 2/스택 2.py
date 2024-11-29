import sys

num_list = []
N = int(sys.stdin.readline().strip())
for i in range(N):
    num = sys.stdin.readline().strip().split()
    if num[0] == '1':
        num_list.append(num[1])
    elif num[0] == '2':
        if len(num_list)==0:
            print(-1)
        else:
            print(num_list.pop())
    elif num[0] == '3':
        print(len(num_list))
    elif num[0] == '4':
        if len(num_list)==0:
            print(1)
        else:
            print(0)
    elif num[0] == '5':
        if len(num_list)==0:
            print(-1)
        else:
            print(num_list[-1])