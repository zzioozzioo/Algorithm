import sys

input = sys.stdin.readline

def factorial(x):
    if x==0 or x==1:
        return 1
    return (x*factorial(x-1))

N = int(input().rstrip())

print(factorial(N))