num_list = sorted(list(map(int, input().split())))

if num_list[0]+num_list[1] <= num_list[2]:
    print((num_list[0]+num_list[1])*2 - 1)
else:
    print(sum(num_list))