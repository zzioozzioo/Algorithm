import sys

N, M = map(int, sys.stdin.readline().split())
n_set = set()
count = 0

for _ in range(N):
    n_set.add(sys.stdin.readline().rstrip())

for _ in range(M):
    data = sys.stdin.readline().rstrip()
    if data in n_set:
        count += 1

print(count)

# import sys

# N, M = map(int, sys.stdin.readline().split())
# dic = {}
# count = 0

# for _ in range(N):
#     data = sys.stdin.readline().rstrip()
#     dic[data] = True

# for _ in range(M):
#     data = sys.stdin.readline().rstrip()
#     if data in dic:
#         count += 1
    
# print(count)