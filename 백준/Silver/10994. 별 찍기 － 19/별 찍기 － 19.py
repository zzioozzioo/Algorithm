def draw(n, x, y):
    if n == 1:
        arr[x][y] = '*'
        return
    
    size = 4*n - 3
    end = size - 1

    for i in range(size):
        arr[x][y+i] = '*'       # 위
        arr[x+end][y+i] = '*'   # 아래
        arr[x+i][y] = '*'       # 왼쪽
        arr[x+i][y+end] = '*'   # 오른쪽

    draw(n-1, x+2, y+2)

N = int(input())
size = 4*N - 3
arr = [[' '] * size for _ in range(size)]

draw(N, 0, 0)

for row in arr:
    print(''.join(row))