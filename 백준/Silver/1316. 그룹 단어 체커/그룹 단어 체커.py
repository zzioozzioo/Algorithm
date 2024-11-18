N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(len(word)-1): # len(word)-1인 이유는 길이=인덱스+1이기 때문~!
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)