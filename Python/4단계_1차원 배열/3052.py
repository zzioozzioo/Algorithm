n = list(range(1, 11))

for i in range(1, 11):
    num = int(input())
    if num%42 not in n:
        n.append(num%42)
print(len(n))


# arr = []
# for i in range(10):
#     a = int(input())
#     arr.append(a % 42)
# print(len(set(arr)))