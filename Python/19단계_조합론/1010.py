import sys
sys.setrecursionlimit(10**7)

def factorial(x):
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)

# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num

T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(factorial(M) // factorial(N) // factorial(M-N))
    math.factorial(M) // (math.factorial(N) * math.factorial(M - N))