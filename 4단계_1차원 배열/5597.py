n = [i for i in range(1, 31)]

for i in range(1, 29):
    num = int(input())
    n.remove(num)

print(min(n))
print(max(n))