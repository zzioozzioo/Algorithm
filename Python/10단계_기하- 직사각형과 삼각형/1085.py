x, y, w, h = map(int, input().split())
x_dis = 0
y_dis = 0

if x > w/2:
    x_dis = w-x
else:
    x_dis = x

if y > h/2:
    y_dis = h-y
else:
    y_dis = y

print(min(x_dis, y_dis))


# 다른 풀이
# x, y, w, h = map(int, input().split())
# print(min(x, y, w-x, h-y))