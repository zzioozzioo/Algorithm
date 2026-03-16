from math import gcd

n = int(input())
list = [] # 약수 저장할 리스트

if n == 2:
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)

if n == 3: 
    a, b, c = map(int, input().split())
    gcd_num = gcd(a, b, c)

for i in range(1, int(gcd_num**0.5)+1):
    if gcd_num%i == 0:
        list.append(i)
        
        if list.count(gcd_num//i) == 0:
            list.append(gcd_num//i)

list.sort()
print(*list, sep='\n')