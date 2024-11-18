import sys

input = sys.stdin.readline

N = int(sys.stdin.readline().rstrip())
num_list = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)

print(round(sum(num_list)/len(num_list)))

num_list = sorted(num_list)
print(num_list[int(N//2)])

dic = dict() # 각 숫자의 빈도 저장할 딕셔너리
for i in num_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_num = max(dic.values()) # 빈도수 저장한 dic에서 최대값(최빈값) 구하기
max_dic = [] # 가장 많이 등장한 최빈갑(숫자)을 저장할 배열

for i in dic: # 최빈값이 여러 개인 경우를 찾기 위함
    if max_num == dic[i]:
        max_dic.append(i)

if len(max_dic) > 1: # 최빈값이 여러 개인 경우
    print(max_dic[1])
else:
    print(max_dic[0])

print(int(max(num_list)-min(num_list)))
