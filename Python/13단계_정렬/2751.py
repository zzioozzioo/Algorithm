import sys

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
for i in num_list:
    print(i) 


# 이건 나중에 진짜 알고리즘이랑 비교해보기
# for i in range(N):
#     if num_list[i] < num_list[i+1]: # 오름차순인 경우
#         continue
#     else:
#         num = num_list[i]
#         num_list[i] = num_list[i+1]
#         num_list[i+1] = num