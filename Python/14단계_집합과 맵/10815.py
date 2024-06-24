import sys

N = int(sys.stdin.readline()) # 숫자 카드의 개수
card_list = list(map(int, sys.stdin.readline().split())) # 상근 카드

M = int(sys.stdin.readline()) # 맞출 카드 개수
num_list = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in num_list:
    dic[i] = 0 # 딕셔너리 초기화

for i in card_list:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end=' ')


# import bisect

# N = int(input())
# card_list = list(map(int, input().split()))

# M = int(input())
# num_list = list(map(int, input().split()))

# card_list.sort()
# result = [0]*M

# for i in num_list:
#     l = bisect.bisect_left(card_list, i)
#     r = bisect.bisect_right(card_list, i)
#     print(r-l, end=' ')