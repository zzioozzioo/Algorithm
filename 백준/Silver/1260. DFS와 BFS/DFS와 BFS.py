N, M, start = map(int, input().split())

# 그래프 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list = []
def dfs(node):
    # 방문했다고 표시 -> 방문한 노드를 모아놓는 리스트 활용
    visited_list.append(node)

    # 할 일 하기
    print(node, end=' ')
    for adj_node in sorted(graph[node]):
        # list.sort(): in-place sort - 제자리 정렬
        # sorted(list): 원본 데이터가 변경
        if adj_node not in visited_list:
            dfs(adj_node)

from collections import deque

queue = deque()
def bfs(start):
    queue.append(start)  
    while queue:
        node = queue.popleft()
        visited_list.append(node)  # 방문했다고 표시
        print(node, end=' ')                # 할 일 하기 (objective)
        for adj_node in sorted(graph[node]):
            if adj_node not in visited_list:
                # print('>>>>', adj_node)
                if adj_node not in queue:
                    queue.append(adj_node)     # 순회시킬 노드로 등록하기 to queue

dfs(start)
print()
visited_list.clear()
bfs(start)