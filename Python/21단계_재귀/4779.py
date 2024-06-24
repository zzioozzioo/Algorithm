# import math
import sys

input = sys.stdin.readline

def Cantor(start, len):
    # line.remove(line[(3**N)*(1/3):(3**N)*(2/3)+1:]) # 가운데 구간 삭제 

    if len == 1:
        return
    for i in range(start+len//3, start+(len//3)*2):
        line[i] = ' ' # 가운데 문자열(1/3~2/3 구간)을 공백으로 변경
    Cantor(start, len//3)
    Cantor(start+len//3*2, len//3)

while True:
    try:
        N = int(input().rstrip())
        line = ['-']*(3**N) # 최초 리스트
        Cantor(0, 3**N)
        print(''.join(line))   
    except EOFError:
        break

