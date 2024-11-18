import sys

input = sys.stdin.readline
N, M = map(int, input().split())

int_key = {} # key값이 int인 dictionary
name_key = {} # key값이 str인 dictionary

# 포켓몬 저장
for i in range(1, N+1):
    data = input().strip()
    int_key[i] = data # key: 번호, value: 포켓몬 이름
    name_key[data] = i # key: 포켓몬 이름, value: 번호

# 포켓몬 탐색
for _ in range(M):
    data = input().strip()

    if data.isdigit() == True: # isdigit(): 숫자로만 이루어져 있는지 판별, 맞으면 True
        print(int_key[int(data)])
    else:
        print(name_key[data])