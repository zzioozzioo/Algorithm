import sys

N = int(sys.stdin.readline())
arr = [0] * (10000+1) # 리스트를 [0] * (데이터의 길이 + 1)만큼 선언

# 각 입력값에 해당하는 인덱스의 값 증가
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1 # 해당 인덱스의 갯수(횟수) 세는 것!

# arr에 기록된 값 출력
for i in range(len(arr)):
    if arr[i] != 0: # 입력값 각각의 횟수가 0개가 아닌 경우
        for _ in range(arr[i]):
            print(i)