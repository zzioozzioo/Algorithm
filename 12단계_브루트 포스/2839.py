N = int(input())
num_list = []

for i in range(N):
    for j in range(N):
        if 5*i+3*j == N:
            num_list.append(i+j)
if len(num_list) != 0:
    print(min(num_list))
else:
    print(-1)
