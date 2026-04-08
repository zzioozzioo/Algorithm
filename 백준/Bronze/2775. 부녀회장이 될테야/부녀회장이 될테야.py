import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호

    residents = [i for i in range(1, n+1)] # 0층(1~n호) 데이터로 초기화
    for _ in range(k):
        for j in range(1, n):
            residents[j] += residents[j-1]
    print(residents[-1])
    