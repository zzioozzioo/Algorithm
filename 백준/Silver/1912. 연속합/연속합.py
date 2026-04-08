import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

current_max = 0
dp = [0] * n
dp[0] = num_list[0]
count = 0
for i in range(1, n):
    if num_list[i] < 0:
        count += 1
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])

# 모두 음수인 경우 처리
if count == len(num_list):
    abs_max = num_list[0]
    for num in num_list:
        if abs(num) < abs(abs_max): # 절댓값 작은 게 큰 값
            abs_max = num
    current_max = abs_max
else:
    current_max = max(dp)

print(current_max)