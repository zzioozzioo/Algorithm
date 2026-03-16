def factorial(num):
    # 재귀로 구현
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

n = int(input())

k = n//3-1
result = factorial(k) // (factorial(2)*factorial(k-2))

print(result)