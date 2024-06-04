import sys

input = sys.stdin.readline
N = int(input().strip())
n_list = list(map(int, input().strip().split()))
M = int(input().strip())
m_list = list(map(int, input().strip().split()))
card = {} # n_list 원소 개수 구하는 딕셔너리

for i in n_list:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

for i in m_list:
    if i in card:
        print(card[i], end=' ')
    else:
        print(0, end=' ')