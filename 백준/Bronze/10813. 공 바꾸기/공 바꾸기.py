n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

temp = 0
for x in range(0, m):
    i, j = map(int, input().split())
    temp = basket[i-1] 
    basket[i-1] = basket[j-1]
    basket[j-1] = temp
    x += 1

for i in range(n):
    print(basket[i], end=' ')