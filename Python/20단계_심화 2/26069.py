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

# import sys

# input = sys.stdin.readline

# N = int(input().rstrip())
# name_set = {'ChongChong'} # 집합 자료형 선언 및 원소 삽입

# for i in range(N):
#     A, B = input().rstrip().split()

#     if A in name_set:
#         name_set.add(B)

#     if B in name_set:
#         name_set.add(A)

# print(len(name_set))