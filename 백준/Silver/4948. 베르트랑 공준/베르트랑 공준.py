import sys

num = 123456*2 + 1
num_list = [1]*num # 전체를 1로 초기화

for i in range(1, num):
    if i == 1:
        num_list[1] = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0: # 소수이면 0 저장
            num_list[i] = 0
            break

while True:
    n = int(sys.stdin.readline().strip())

    if n==0:
        break

    print(sum(num_list[n+1:2*n+1]))