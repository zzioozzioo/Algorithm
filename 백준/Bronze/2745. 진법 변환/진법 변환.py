alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

N, B = input().split()
B = int(B) # 몇진법인지 정수로 변환
N = N[::-1]

for i, j in enumerate(N):
    sum += (alphabet.index(j) * (B**i))

print(sum)
