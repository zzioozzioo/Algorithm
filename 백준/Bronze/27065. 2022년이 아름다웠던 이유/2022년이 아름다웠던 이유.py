def get_sum_of_divisor(num):
    sum = 0
    for i in range(1, num//2+1): # 약수의 합
            if num%i == 0:
                sum += i
    return sum

T = int(input())

for i in range(T):
    target = int(input()) # 과잉수 판별할 수
    flag = False # 조건에 맞지 않는 경우를 기본값으로
    if target < get_sum_of_divisor(target): # 과잉수인 경우
        for j in range(1, target): # 약수의 부족수/완전수 판단
            if target%j == 0: 
                if j < get_sum_of_divisor(j): # 약수이면서 과잉수인 경우
                    flag = False
                    break
                else:
                    flag = True
    
    if flag:
        print("Good Bye")
    else:
        print("BOJ 2022")    
