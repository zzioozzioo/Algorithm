chess = [1, 1, 2, 2, 2, 8]
dh = list(map(int, input().split()))

for i in len(chess):
    print(chess[i] - dh[i], end = ' ')

# for i in len(chess):
#     print(chess[i], end=' ')
        