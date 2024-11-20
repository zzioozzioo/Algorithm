word = input()
str = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = 0

for i in range(len(word)):
    for j in str:
        if word[i] in j:
            num += str.index(j)+3

print(num)