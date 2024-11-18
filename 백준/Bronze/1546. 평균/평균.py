n = int(input())
score = list(map(int, input().split()))
# for i in range(n):
#     score[i] = int(input())
m = max(score)
for i in range(n):
    score[i] = score[i]/m*100

print(sum(score)/n)