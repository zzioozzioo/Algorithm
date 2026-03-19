L = int(input())

p_count = 1 # 피노키오의 종류 개수
acgt_count = 0
string = list(input()) # 'AACGT'
list = ['A', 'G', 'C', 'T'] # 염기쌍 한세트

for i in list: # 입력 문자열 돌면서
    i_count = string.count(i)

    # 모든 염기가 존재하는지 판별하기
    if i_count == 0:
        p_count = 0
        break
    
    if i_count >= 2: # 각 염기의 수가 2개 이상인 경우
        p_count *= i_count       
    
print(p_count%1000000007)
        