sum = 0
numList = list(map(int, input().split()))
for num in numList:
    sum += num**2

print(sum%10)