import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

index = 0
queue = [i for i in range(1, N+1)]

person = []
while queue: # 원소가 존재하는 동안
    index += K-1
    if index >= len(queue): # 인덱스가 범위를 넘어갈 경우
        index %= len(queue)
    person.append(str(queue.pop(index)))

print('<' + ', '.join(person) + '>')
