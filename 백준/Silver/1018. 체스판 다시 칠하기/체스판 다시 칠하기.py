N, M = map(int, input().split())
list = []
count = []

for _ in range(N):
    list.append(input())

for i in range(N-7): # 전체 체스판에서 시작점을 잡기 위한 반복문 1 (i: 행 시작점)
    for j in range(M-7): # 전체 체스판에서 시작점을 잡기 위한 반복문 2 (j: 열 시작점)
        index1 = 0 # 'W'로 시작할 경우 바뀔 체스판의 갯수 count
        index2 = 0 # 'B'로 시작할 경우 바뀐 체스판의 갯수 count

        for a in range(i, i+8):
            for b in range(j, j+8):
                # 짝+홀인 경우에만 홀수, 나머지는 짝수
                if (a+b)%2 == 0: # 짝수인 경우 
                    if list[a][b] != 'W':
                        index1 += 1 # 체스판 하나 바꿔야 함
                    if list[a][b] != 'B':
                        index2 += 1
                else: # 홀수인 경우
                    if list[a][b] != 'B':
                        index1 += 1 # 체스판 하나 바꿔야 함
                    if list[a][b] != 'W':
                        index2 += 1

        count.append(min(index1, index2))

print(min(count))