import sys

N = int(sys.stdin.readline())
member_list = []

for _ in range(N):
    [age, name] = list(sys.stdin.readline().split())
    age = int(age)
    member_list.append([age, name])

member_list.sort(key=lambda x: (x[0]))

for i in member_list:
    print(i[0], i[1])
