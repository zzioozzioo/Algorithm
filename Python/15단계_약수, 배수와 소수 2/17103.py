import sys

primeNum = [0]*2 + [1]*999999

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(2*i, 1000001, i):
            primeNum[j] = 0

T = int(sys.stdin.readline().strip())

for i in range(T):
    count = 0
    N = int(sys.stdin.readline().strip())
    for j in range(2, N//2+1): # N//2+1인 이유: 중복값 제거하기 위함!! (작은 값을 j로 설정함)
        if primeNum[j] and primeNum[N-j]:
            count += 1
    print(count)