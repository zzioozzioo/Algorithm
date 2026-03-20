N = int(input())

# 1~5번째 줄
for i in range(N):
    # 공백
    print(' '*i, end='')

    # 별
    print('*'*(2*N-2*i-1))
    # i=1 -> 9 -> 10-1
    # i=2 -> 7 -> 10-3
    # i-3 -> 5 -> 10-5
    # i=4 -> 3 -> 10-7
    # i=5 -> 1 -> 10-9

# 6~9번째 줄
for i in range(1, N):
    # 공백
    print(' '*(N-i-1), end='')

    # 별
    print('*'*(2*i+1))

