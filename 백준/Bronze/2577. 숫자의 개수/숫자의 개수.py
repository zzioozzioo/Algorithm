result = 1
count = [0]*10

for _ in range(3):
		result *= int(input())

result = str(result)
for i in result:
    count[int(i)] += 1

for i in count:
    print(i)