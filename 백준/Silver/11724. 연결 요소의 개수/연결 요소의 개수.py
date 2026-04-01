import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

num_node, num_edge = map(int, input().split())
graph = [[] for _ in range(num_node+1)]

for _ in range(1, num_edge+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list = [False] * (num_node+1)

def dfs(node):
    visited_list[node] = True
    
    for adj_node in graph[node]:
        if visited_list[adj_node] == False:
            dfs(adj_node)

count = 0
for i in range(1, num_node+1):
    if visited_list[i] == False: # 방문하지 않은 노드
        dfs(i) # 
        count += 1

print(count)