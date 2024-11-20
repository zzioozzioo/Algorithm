n = []

for i in range(1, 11):
    num = int(input())
    if num%42 not in n:
        n.append(num%42)
print(len(n))
