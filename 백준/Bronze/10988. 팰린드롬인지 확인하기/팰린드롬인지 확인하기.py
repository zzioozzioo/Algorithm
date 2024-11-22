word = input()
new_word = word[::-1]
num = 0

for i in range(len(word)):
    if word[i] == new_word[i]:
        num += 1

if len(word) == num:
    print(1)
else:
    print(0)