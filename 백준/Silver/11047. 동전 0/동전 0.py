N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))
    coin.sort()
    coin.reverse() # 큰 가치의 동전부터 내림차순

coin_num = 0
while K != 0: # 나누어 떨어지면 종료
    for c in coin:
        if K >= c:
            coin_num += K//c
            K %= c

print(coin_num)