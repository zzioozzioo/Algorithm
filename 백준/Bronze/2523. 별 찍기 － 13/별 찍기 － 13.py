N = int(input())

# 1~3번째 줄
for i in range(1, N+1):
    print('*'*i)

# 4~5번째 줄
for i in range(N-1, 0, -1):
    print('*'*i)