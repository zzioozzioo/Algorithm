N = int(input())
list = []

i = 2
while N != 1:
    if N%i == 0:
        list.append(i)
        N //= i
    else:
        i += 1

if len(list) > 0:
    for i in list:
        print(i)