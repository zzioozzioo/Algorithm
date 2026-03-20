N = int(input())

# 1~3번째 줄
for i in range(N):
    # 공백
    print(' '*(N-i-1), end='')

    # 별
    print('*'*(i+1))

# 4~5번째 줄
for i in range(1, N):
    # 공백
    print(' '*i, end='')

    # 별
    print('*'*(N-i))