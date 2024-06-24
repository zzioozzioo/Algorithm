list = []
for _ in range(3):
    a = int(input())
    list.append(a)

flag = 0
for i in range(3):
    if list.count(list[i]) == 2:
        flag = 2
    elif list.count(list[i]) == 1:
        flag = 1


if sum(list) != 180:
    print('Error')
elif flag == 2:
    print('Isosceles')
elif flag == 1:
    print('Scalene')
else:
    print('Equilateral')