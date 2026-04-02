N = int(input())

# 자료구조 정의
# 5kg, 3kg의 최대 봉지 수
max_5kg = N//5
max_3kg = N//3
min_bag = max_5kg + max_3kg

is_found = False

# 알고리즘
for num_5kg in range(0, max_5kg+1):
    for num_3kg in range(0, max_3kg+1):
        if num_5kg*5 + num_3kg*3 == N:
            is_found = True
            cur_bag = num_3kg + num_5kg
            if min_bag > cur_bag:
                min_bag = cur_bag

if is_found:
    print(min_bag)
else:
    print(-1)