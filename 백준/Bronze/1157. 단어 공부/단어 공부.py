word = input().upper()
word_list = list(set(word)) # word_list = ['m', 'i', 's', 'p']

cnt = [] 
for i in word_list:
    count = word.count(i) 
    cnt.append(count) # cnt = [1, 4, 4, 1]

if cnt.count(max(cnt)) > 1: 
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])