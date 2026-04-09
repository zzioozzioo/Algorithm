from collections import deque

def bfs(N, K):

    # 소요 시간 dist
    dist = [-1] * 100001
    dist[N] = 0

    queue = deque([N])

    while queue:
        curr = queue.popleft()

        if curr == K:
            return dist[curr]

        for next_pos in (curr-1, curr+1, curr*2):

            # 범위 내이면서 아직 방문 X
            if 0 <= next_pos <= 100000 and dist[next_pos] == -1:
                dist[next_pos] = dist[curr] + 1
                queue.append(next_pos)       

N, K = map(int, input().split())
print(bfs(N, K))