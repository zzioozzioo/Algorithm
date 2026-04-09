import sys
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    words.add(input().strip())

words = sorted(words, key=lambda x: (len(x), x))
print('\n'.join(words))