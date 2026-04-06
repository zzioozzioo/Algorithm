import sys
input = sys.stdin.readline

# inorder()
# 레벨별로 줄바꿈해서 출력

K = int(input())
num_list = list(map(int, input().split()))

levels = [[] for _ in range(K)] # 레벨 K까지 각 레벨의 트리 결과

def complete_binary_tree(list, depth):
    if not list:
        return
    
    # 루트 노드
    mid = len(list)//2 
    levels[depth].append(list[mid])

    # 왼쪽 서브트리
    complete_binary_tree(list[:mid], depth+1)

    # 오른쪽 서브트리
    complete_binary_tree(list[mid+1:], depth+1)

complete_binary_tree(num_list, 0)

for level in levels:
    print(*level)