words = []

for _ in range(5):
    words.append(input())

for j in range(max(len(word) for word in words)):
    for i in range(5):
        if j < len(words[i]): # j보다 i번째 문자의 길이가 길면(j번째 위치에 문자가 있으면ㅊ
            print(words[i][j], end='')
