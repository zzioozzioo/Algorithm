import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parents = [0] * (N + 1)

queue = deque([1])
parents[1] = -1

while queue:
    node = queue.popleft()
    
    for adj_node in adj[node]:
        if parents[adj_node] == 0:
            parents[adj_node] = node
            queue.append(adj_node)

for i in range(2, N+1):
    print(parents[i])