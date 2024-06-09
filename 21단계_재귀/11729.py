import sys
from collections import deque

input = sys.stdin.readline

def hanoi(n, start, end):
    if n == 1: # 하나밖에 없으면 3번으로 옮기고 끝
        print(start, end)
        return
    
    # 원판이 두 개 이상이면 재귀적 진행
    # 6-start-end: 전체 막대의 번호 합 - from 막대 - to 막대 = 나머지 한 막대
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)


N = int(input().rstrip())
print(2**N-1)
hanoi(N, 1, 3)


