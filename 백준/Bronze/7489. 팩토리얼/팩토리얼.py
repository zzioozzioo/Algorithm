def factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

t = int(input())

for _ in range(t):
    num = int(input())
    result = factorial(num)
    
    while str(result)[-1] == '0':
        result = result//10
    
    print(str(result)[-1])

