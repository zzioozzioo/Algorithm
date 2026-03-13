word = input()

sum = 0
for i in word:
    if i.islower(): # 소문자인 경우
        sum += ord(i)-96
    else:
        sum += ord(i)-38
    
for i in range(2, sum):
    if sum%i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")
