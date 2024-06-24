import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
for i in range(n):
	p = deq.popleft() # pop(0)과 같은 결과를 가져오지만, pop(0)보다 더 빠르다
	print(p[0], end=' ')
	if p[1] > 0:
		deq.rotate(-(p[1] - 1)) # popleft된 1칸을 제외하고 시계 반대방향으로 회전
	else:
		deq.rotate(-p[1]) # 시계 방향으로 회전

# # 다른 풀이 1 - enumerate(), list() 사용 - 시간복잡도 O(N)
# import sys
# input = sys.stdin.readline

# N = int(sys.stdin.readline().rstrip())
# data = list(enumerate(map(int, sys.stdin.readline().rstrip().split()), start=1))

# index = 0 # 첫 번째 index 고정
# while data:
#     value = data.pop(index)
#     print(value[0], end=' ')
#     if value[1] < 0 and data: # 다음 인덱스 위치가 음수이고 리스트에 원소가 남아있으면
#         index = (index+value[1]) % len(data)
#     elif value[1] > 0 and data:
#         index = (index+value[1]-1) % len(data)

# # 다른 풀이 2 - enumerate(), deque(), rotate() 사용
# import sys
# from collections import deque

# input = sys.stdin.readline()

# N = int(sys.stdin.readline().rstrip())
# deq = deque(enumerate(map(int, sys.stdin.readline().rstrip().split())))
# result = []

# while deq:
#     index, paper_num = deq.popleft()
#     result.append(index+1)

#     if paper_num > 0:
#         deq.rotate(-(paper_num-1))
#     else:
#         deq.rotate(-paper_num)

# print(' '.join(map(str, result)))