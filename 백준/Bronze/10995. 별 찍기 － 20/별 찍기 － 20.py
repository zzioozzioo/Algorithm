N = int(input())

for i in range(1, N+1):
    if i%2==0:
        print(' *'*N)
    elif N == 1:
        print('*')
    else:
        print('* '*N)