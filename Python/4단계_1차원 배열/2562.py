a = []
for i in range(0, 9):
    a.append(int(input()))
    i += 1
print(max(a))
for i in range(0, 9):
    if max(a) == a[i]:
        print(i+1)
    else: i += 1