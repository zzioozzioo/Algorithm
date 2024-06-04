import sys

input = sys.stdin.readline
N = int(input().rstrip())

gomgom = set()
count = 0

for i in range(N):
    line = sys.stdin.readline().rstrip()

    if line == 'ENTER':
        gomgom.clear()
    else:
        if line not in gomgom:
            count += 1
            gomgom.add(line)

print(count)
