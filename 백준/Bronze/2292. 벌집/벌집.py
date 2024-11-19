N = int(input())
num = 1 # 초기 숫자 1의 벌집 갯수는 1개
layer = 1 # 몇 번째 layer

while N > num:
    num += 6*layer # 한 layer마다 방의 개수는 6의 배수로 증가
    layer += 1

print(layer)