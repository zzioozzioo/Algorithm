phoneNum, new = map(int, input().split())

flag_a, flag_b = True, True # 소수라고 가정
for i in range(2, phoneNum//2+1):
    if phoneNum%i == 0:
        flag_a = False # 약수가 있으므로 소수가 아님

newNum = int(str(new)+str(phoneNum))

for i in range(2, newNum//2+1):
    if newNum%i == 0:
        flag_b = False # 소수가 아님

if flag_a and flag_b:
    print("Yes")
else:
    print("No")