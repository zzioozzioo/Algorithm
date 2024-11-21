import sys

K = int(sys.stdin.readline().strip())
num_list = []

for i in range(K):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

print(sum(num_list))
