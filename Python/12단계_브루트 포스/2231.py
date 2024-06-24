N = int(input())
num_list = []
sum_i = 0
for i in range(1, N+1):
    sum_i = sum(map(int, str(i)))
    if N == sum_i + i:
        num_list.append(i)

if len(num_list) == 0:
    print(0)
else:
    print(min(num_list))


# 다른 방식
# n = int(input())
# for i in range(n):
#     # 분해합 공식
#     digit_sum = i + sum(map(int, str(i)))
#     # 생성자일 경우
#     if digit_sum == n:
#         print(i)
#         break
# else:
#     print(0)

