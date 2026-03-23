N = int(input())

# N만큼 패턴 반복하기
for _ in range(N):
    # 윗층
    print('* '*(N-(N//2)))
    
    # 아랫층
    print(' *'*(N//2))