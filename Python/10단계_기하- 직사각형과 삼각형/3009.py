a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x, y = 0, 0

if a==c:
    x = e
elif a==e:
    x = c
else:
    x = a

if b==d:
    y = f
elif b==f:
    y = d
else:
    y = b

print(x, y)


# 다른 풀이

# x_points = []
# y_points = []

# for _ in range(3):
#     x, y = map(int, input().split())
#     x_points.append(x)
#     y_points.append(y)

# for i in range(3):
#     if x_points.count(x_points[i]) == 1:
#         x4 = x_points[i]
#     if y_points.count(y_points[i]) == 1:
#         y4 = y_points[i]

# print(x4, y4)