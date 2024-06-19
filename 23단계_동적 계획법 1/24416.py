import sys
input = sys.stdin.readline

def fib(n):
    if n == 1 or n ==2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def fibonacci(n):
    f = [0] * (n+1) # n+1개인 이유: index 1부터 n까지 사용하는데 0은 제외하고 시작하므로!
    f[1], f[2] = 1, 1
    count = 0
    for i in range(3, n+1):
        count += 1
        f[i] = f[i-1] + f[i-2]
    return count


n = int(input().rstrip())
print(fib(n), fibonacci(n))

# # 다른 풀이
# import sys
# input = sys.stdin.readline

# def fib(n):
#     a, b = 1, 1
#     for i in range(3, n+1):
#         a, b = b, a+b

# def fibonacci(n):
#     return n-2    

# n = int(input().rstrip())
# print(fib(n), fibonacci(n))
