N = int(input())

# 1~5번째 줄
for i in range(1, N+1):
    # 별
    print('*'*i, end='')

    # 공백
    print(' '*(2*N-2*i), end='')

    # 별
    print('*'*i, end='')
    print()

# 6~9번째 줄
for i in range(N-1, 0, -1):
    # 별
    print('*'*i, end='')

    # 공백
    # i=4 -> 공백 2
    # i=3 -> 공백 4
    # i=2 -> 공백 6
    # i=1 -> 공백 8
    print(' '*(2*(N-i)), end='')

    # 별
    print('*'*i, end='')
    print()
