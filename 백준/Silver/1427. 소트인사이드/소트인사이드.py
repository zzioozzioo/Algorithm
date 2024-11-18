import sys

N = int(sys.stdin.readline())
list = []

for i in range(len(str(N))):
    list.append(str(N)[i])

list = sorted(list, reverse=True)

for i in list:
    print(i, end='')
