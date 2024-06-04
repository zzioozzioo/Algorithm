N, k = map(int, input().split())
score_list = list(map(int, input().split()))
score_list = sorted(score_list, reverse=True)
print(score_list[k-1])
