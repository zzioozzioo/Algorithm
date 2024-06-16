import sys
input = sys.stdin.readline

def queen(k): # k: 놓은 말 개수
    global N, count

    if k == N: # 놓은 말 개수와 N이 같을 때(주어진 말이 다 놓아졌을 때)
        count += 1
        return
    
    for i in range(N):
        if not used_c[i] and not used_up[k+i] and not used_down[k-i+(N-1)]:
            # used_c[i]가 비어있고, 그 왼쪽 아래 대각선인 used_up[k+i]가 비어있고,
            # 또한 오른쪽 아래 대각선인 used_down[k-i+(N-1)]가 비어있다면
                used_c[i] = True 
                used_up[k+i] = True
                used_down[k-i+(N-1)] = True
                # 세 가지 위치에 퀸 놓을 수 있음!

                queen(k+1) # 다음 행으로 내려가면서 열, 양쪽 대각선 False로 초기화
                used_c[i] = False
                used_up[k+i] = False
                used_down[k-i+(N-1)] = False


N = int(input().rstrip())
maps = [[0] * N for i in range(N)] # N*N 크기의 2차원 배열 생성

# True: 점유 / False: 비점유
used_c = [False]*N # 열 점유 여부
used_up = [False]*(2*(N-1)+1) # 왼쪽 아래 대각선 (y = x) 선상 점유 여부
used_down = [False]*(2*(N-1)+1) # 오른쪽 아래 대각선 (y = -x) 선상 점유 여부

count = 0

queen(0) # 놓은 말 개수 0개부터 시작
print(count)