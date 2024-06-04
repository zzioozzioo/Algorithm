import sys

input = sys.stdin.readline
M, N = map(int, input().split())

def check(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0: # 소수가 아닌 경우
            return False
    return True # 소수인 경우

for i in range(M, N+1):
    if i == 1:
        continue
    if check(i): # 소수인 경우
        print(i)