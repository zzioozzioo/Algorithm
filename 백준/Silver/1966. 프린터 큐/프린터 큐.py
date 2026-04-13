from collections import deque

def solve():
    N, M = map(int, input().split())

    priorities = list(map(int, input().split()))
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    count = 0
    while queue:
        targetNum = queue.popleft()

        if any(targetNum[0] < num[0] for num in queue): # 우선순위가 높은 문서가 있는 경우
            queue.append(targetNum) # 가장 뒤에 재배치
            
        else:
            count += 1
            if targetNum[1] == M:
                return count

T = int(input())

for _ in range(T):
    print(solve())