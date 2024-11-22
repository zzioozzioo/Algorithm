N, K = map(int, input().split())

def factorial(x):
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)

print(factorial(N) // factorial(K) // factorial(N-K))

