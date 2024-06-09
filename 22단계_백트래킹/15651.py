# 중복순열(nㅠr): N개 중 중복 허용하고 M개 선택(순서 상관 있음)

import sys
import itertools # 조합 라이브러리
input = sys.stdin.readline

def combination(n, r):
    num_list, result = [], []
    for i in range(1, n+1):
        num_list.append(i)
    result = itertools.product(num_list, repeat=r)
    for i in result:
        for j in range(r):
            print(i[j], end=' ')
        print()

N, M = map(int, input().rstrip().split())
list = [] # 수열 저장
combination(N, M)
