import sys

input = sys.stdin.readline
n = int(input())
dic = {}

for i in range(n):
    name, el = input().rstrip().split()
    if el == 'enter':
        dic[name] = el
    else:
        del dic[name]
    
dic = sorted(dic.keys(), reverse=True) # 키 값을 정렬하는데 사전 역순을 기준으로!

for i in dic: # dictionary에서는 키 값으로 도니까 
    print(i) # 그 키 값(이름)을 출력
