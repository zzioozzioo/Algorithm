import sys

input = sys.stdin.readline
n = int(input().strip())

def check(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0: # 소수가 아닌 경우
            return False
    return True # 소수인 경우

for i in range(n):
    num = int(input().strip())

    while True:
        if num==0 or num==1:
            print(2)
            break
        if check(num):
            print(num)
            break
        else:
            num += 1               