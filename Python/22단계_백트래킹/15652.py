# 중복조합(nHr): N개 중 중복 허용하고 M개 선택(순서 상관 없음)

import sys
import itertools # 조합 라이브러리
input = sys.stdin.readline

def combination(n, r):
    num_list, result = [], []
    for i in range(1, n+1):
        num_list.append(i)
    result = itertools.combinations_with_replacement(num_list, r)
    for i in result:
        for j in range(r):
            print(i[j], end=' ')
        print()

N, M = map(int, input().rstrip().split())
list = [] # 수열 저장
combination(N, M)

# # itertools 사용하지 않고 구현
# import sys

# input = sys.stdin.readline

# def combination_with_replacement(n, r):
#     for i in range(len(n)):
#         if r == 1: # 종료조건. 1개만 뽑을 때
#             yield [n[i]]
#         else:
#             for j in combination_with_replacement(n[i:], r-1): 
#                 # 한 명을 뽑았다고 가정하고, 
#                 # 이전에 뽑은 것은 허용하지 않고(그래서 n[i]부터 뽑기 가능) 뽑기
#                     yield[n[i] + j] # n[i]가 위에서 뽑았다고 가정한 그 한 명!

# N, M = map(int, input().rstrip().split())
# for i in combination_with_replacement(N, M):
#     print(i)
