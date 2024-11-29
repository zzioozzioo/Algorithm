import sys

input = sys.stdin.readline

name_set = set()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    A, B = sys.stdin.readline().rstrip().split()
    if A=='ChongChong' or B=='ChongChong':
        name_set.add(A)
        name_set.add(B)
    if A in name_set or B in name_set:
        name_set.add(A)
        name_set.add(B)

print(len(name_set))
