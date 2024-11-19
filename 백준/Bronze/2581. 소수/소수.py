M = int(input())
N = int(input())
list = []

for j in range(M, N+1):
    no_prime = 0
    if j > 1:
        for i in range(2, j):
            if j%i == 0: # 소수가 아닌 경우
                no_prime += 1
                break
        
        if no_prime == 0: # 소수인 경우
            list.append(j)

if len(list) > 0:
    print(sum(list))
    print(min(list))
else:
    print(-1)