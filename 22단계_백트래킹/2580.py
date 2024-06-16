import sys
input = sys.stdin.readline

def check_row(row, n):
    for i in range(9):
        if n == sudoku[row][i]: # 이미 있으면
            return False
    return True

def check_col(col, n):
    for i in range(9):
        if n == sudoku[i][col]: # 이미 있으면
            return False
    return True 
  
def check_square(row, col, n):
    for i in range(3):
        for j in range(3):
            if n == sudoku[row//3*3+i][col//3*3+j]: # 칸 내에 이미 있으면
                # 각 칸이 시작하는 인덱스를 구함
                # 012 345 678
                # ex) 2 -> 0, 5 -> 3
                return False
    return True

def find(n):
    if n == len(blank):
        # 답을 찾으면(칸을 채운 횟수 == 처음 찾은 빈칸의 횟수일 때) 프로그램 종료
        for i in sudoku:
            print(*i)
        exit()
    
    for i in range(1, 10):
        row = blank[n][0]
        col = blank[n][1]

        if check_row(row, i) and check_col(col, i) and check_square(row, col, i):
            sudoku[row][col] = i
            find(n+1) # 새로운 분기 시작
            sudoku[row][col] = 0 # 분기가 종료되면 (답이 없다면) 원상태로 복구


sudoku = [list(map(int, input().rstrip().split())) for i in range(9)]
blank = [] # 빈칸 위치 체크할 리스트

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])

# 다른 방법: sudoku에 값 입력받고 0인 인덱스는 blank에 추가
# for i in range(9):
#     for j, num in enumerate([int(x) for x in input().rstrip().split()]):
#         sudoku[i].append(num)
#         if num == 0:
#             blank.append([i, j])

find(0)