import sys

input = sys.stdin.readline
N, K = map(int, sys.stdin.readline().rstrip().split())

list = list(range(1, N+1))
# 초기화하는 건 이거랑 동일
# for i in range(1, N+1):
#     list.append(i)

person = [] # 제거된 순서 담는 배열
index = 0
while len(list) != 0:
    index += (K-1)
    index = index % len(list)
    person.append(list.pop(index))

print('<', end='')
for i in range(len(person)-1):
    print(person[i], end=', ')
print(person[-1], end='')
print('>', end='')


# 큐 사용 1
# import sys
# from collections import deque

# N, K = map(int, sys.stdin.readline().rstrip().split())

# # 양방향 연결 리스트(deque) 생성
# deq = deque([i for i in range(1, N+1)])

# # 요세푸스 순열 생성
# person = []
# while len(deq) > 0:
#     for i in range(K-1):
#         deq.append(deq.popleft()) # K번째가 나오기 전까지 deq 맨 뒤로 이동
#     person.append(str(deq.popleft())) # K번째 노드 삭제 후 person 배열에 추가

# print('<' + ', '.join(person) + '>')


# 큐 사용 2
# import sys
# from collections import deque

# N, K = map(int, sys.stdin.readline().rstrip().split())

# index = 0
# queue = [i for i in range(1, N+1)]

# person = []
# while queue: # 원소가 존재하는 동안
#     index += K-1
#     if index >= len(queue): # 인덱스가 범위를 넘어갈 경우
#         index %= len(queue)
#     person.append(str(queue.pop(index)))

# print('<' + ', '.join(person) + '>')
