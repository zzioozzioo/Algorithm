n, m = map(int, input().split())
basket = [0] * n 

for x in range(0, m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        basket[y-1] = k

for i in range(0, n):
    print(basket[i], end=' ')

# for x in range(1, m+1):
#     i, j, k = map(int, input().split())

#     list = []
#     list[0] = 0
#     for a in range(1, n+1):
#         if a == i:
#             for b in range(i, j+1):
#                 list[b] = k
#         else:
#             list[a] = 0
#         a += 1
#     x += 1

# for a in range(1, n+1):
#     print(list[a])