import sys

N = int(input())
word_list = []

for _ in range(N):
    word_list.append(sys.stdin.readline())

word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x), x))

for i in word_list:
    print(i, end='')
