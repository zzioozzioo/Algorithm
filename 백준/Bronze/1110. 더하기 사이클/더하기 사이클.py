n = int(input())
count = 0
new_num = n

while True:
    a = n // 10 # 십의 자리
    b = n % 10 # 일의 자리
    c = (a+b)%10 # 새로운 수의 일의 자리
    n = b*10 + c
    count+=1

    if n == new_num:
        break

print(count)