import math
a, b = map(int, input().split())

# # 최대 공약수
# for i in range(min(a, b)//2, 0, -1):
#     if a%i==0 and b%i==0:
#         print(i)
#         break

# # 최소 공배수
# for i in range(max(a, b), a*b+1):
#     if i%a==0 and i%b==0:
#         print(i)
#         break

# 최대 공약수
print(math.gcd(a,b))


# 최소 공배수
print(math.lcm(a,b))