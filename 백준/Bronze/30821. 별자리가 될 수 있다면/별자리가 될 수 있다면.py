def factorial(num):
    # 재귀로 구현
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

    # 반복문으로 구현
    # result = 1
    # for i in range(2, num+1):
    #     result *= i
    # return result

N = int(input())

# NC5를 구하라
star = factorial(N) // (factorial(5)*factorial(N-5))
print(star)