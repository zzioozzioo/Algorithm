import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def star(len):
    if len == 1: # 1줄만 있으면 그냥 별 하나 출력
        return ['*'] # 근데 1 <= len <= 8로 명시돼 있는데..?
    
    stars = star(len//3)
    list = []

    for i in stars:
        list.append(i*3)
    for i in stars:
        list.append(i + ' '*(len//3) + i)
    for i in stars:
        list.append(i*3)
    
    return list

N = int(input().rstrip())
print('\n'.join(star(N)))