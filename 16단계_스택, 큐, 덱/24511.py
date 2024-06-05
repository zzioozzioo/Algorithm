import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip()) # 자료구조의 개수
A = list(map(int, input().rstrip().split())) # queue or stack을 담는 수열
B = list(map(int, input().rstrip().split())) # 각 자료구조에 들어있는 원소
M = int(input().rstrip()) # queuestack에 삽입할 수열의 길이
C = list(map(int, input().rstrip().split())) # queuestack에 삽입할 원소 담은 수열(길이 M)

queuestack = deque()

for i in range(N):
    if A[i] == 0:
        queuestack.appendleft(B[i])

for i in range(M):
    queuestack.append(C[i])
    print(queuestack.popleft(), end=' ')
# 여기서 포인트: append와 pop의 방향이 다르기만 하면 됨. 들어온 순서대로 나가기만 하면 됨
