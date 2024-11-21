import sys

input = sys.stdin.readline
N = int(input().strip())
n_list = list(map(int, input().strip().split()))
M = int(input().strip())
m_list = list(map(int, input().strip().split()))
card = {} # n_list 원소 개수 구하는 딕셔너리

# 여기서 n_list의 원소 개수를 미리 세두고
for i in n_list:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

# m_list에서 card의 원소가 있으면 해당하는 인덱스의 값(갯수) 출력
for i in m_list:
    if i in card:
        print(card[i], end=' ')
    else:
        print(0, end=' ')