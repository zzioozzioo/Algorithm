N, K = map(int, input().split())

def factorial(x):
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)

print(factorial(N) // factorial(K) // factorial(N-K))

# 다른 방법
# nCk = n-1Ck + n-1Ck-1

# def bino_coef(n, k):
#     if k==0 or n==k:
#         return 1
#     return bino_coef(n-1, k) + bino_coef(n-1, k-1)