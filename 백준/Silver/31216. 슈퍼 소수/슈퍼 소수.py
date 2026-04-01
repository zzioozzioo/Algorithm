import sys
input = sys.stdin.readline

# 1. 에라토스테네스의 체로 충분한 범위의 소수를 미리 구함
MAX = 400000 
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False 

for i in range(2, int(MAX**0.5) + 1): # 2 ~ N의 제곱근까지만 판별
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i): # 배수 지우기
            is_prime[j] = False

# 2. 일반 소수들을 리스트에 담음
primes = []
for i, prime in enumerate(is_prime): # enumerate: (인덱스 번호, 소수 여부)
    if prime == True: # 만약 소수라면
        primes.append(i) # 해당 인덱스(숫자 자체)를 리스트에 추가

# 3. 슈퍼 소수(인덱스+1이 소수인 소수)만 골라냄
super_primes = []
for index, p in enumerate(primes):
    k = index + 1
    if is_prime[k]:
        super_primes.append(p)

# 4. 테스트 케이스 처리
T = int(input())
for _ in range(T):
    n = int(input())
    print(super_primes[n-1])