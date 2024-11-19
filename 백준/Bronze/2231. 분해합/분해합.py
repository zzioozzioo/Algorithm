N = int(input())
num_list = []
sum_i = 0
for i in range(1, N+1):
    # str_i = str(i)
    # for j in range(len(str_i)):
    #     sum += int(str_i[j])
    sum_i = sum(map(int, str(i)))
    if N == sum_i + i:
        num_list.append(i)

if len(num_list) == 0:
    print(0)
else:
    print(min(num_list))
