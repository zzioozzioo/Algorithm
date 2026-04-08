import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

for i in range(len(targets)):
    if targets[i] in A:
        targets[i] = 1
    else:
        targets[i] = 0

print('\n'.join(map(str, targets)))