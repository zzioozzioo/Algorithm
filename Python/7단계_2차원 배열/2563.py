white_paper = [[0] * 100 for _ in range(100)]
sum = 0

num = int(input())
for i in range(num):
    x, y = map(int, input().split())

    for a in range(x, x+10):
        for b in range(y, y+10):
            white_paper[a][b] = 1

for i in white_paper:
    sum += i.count(1)

print(sum)