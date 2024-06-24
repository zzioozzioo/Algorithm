# 순열(nPr): N개 중 중복 허용하지 않고 M개 선택(순서 상관 있음)

import sys
import itertools # 조합 라이브러리
input = sys.stdin.readline

def permutation(n, r):
    num_list, result = [], []
    for i in range(1, n+1):
        num_list.append(i)
    result = itertools.permutations(num_list, r)
    for i in result:
        for j in range(r):
            print(i[j], end=' ')
        print()

N, M = map(int, input().rstrip().split())
list = [] # 수열 저장
permutation(N, M)

# # itertools 사용하지 않고 구현
# import sys

# input = sys.stdin.readline

# def permutation(n, r):
#     for i in range(len(n)):
#         if r == 1: # 종료조건. 1개만 뽑을 때
#             yield [n[i]]
#         else:
#             for j in permutation(n[::i]+n[i+1:], r-1): 
#                 # 한 명을 뽑았다고 가정하고, 
#                 # i-1번째 원소까지 포함하는 리스트 + i+1번째 원소부터 포함하는 리스트
#                 # -> i번째 원소를 포함하지 않고 r-1개를 뽑기
#                     yield[n[i] + j] # n[i]가 위에서 뽑았다고 가정한 그 한 명!

# N, M = map(int, input().rstrip().split())
# for i in permutation(N, M):
#     print(i)