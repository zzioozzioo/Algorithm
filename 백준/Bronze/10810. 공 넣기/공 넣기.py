n, m = map(int, input().split())
basket = [0] * (n) 

for x in range(0, m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        basket[y-1] = k

for i in range(0, n):
    print(basket[i], end=' ')