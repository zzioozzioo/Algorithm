N = int(input())

print(' '*(N-1), '*'*1, sep='') # 동일
for i in range(1, N):
    print(' '*(N-i-1), '*', sep='', end='')
    print(' *'*i)