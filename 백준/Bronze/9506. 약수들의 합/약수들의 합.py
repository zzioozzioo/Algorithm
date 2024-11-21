while True:
    n = int(input())
    if n == -1:
        break
    list = []
    for i in range(1, n):
            if n % i == 0:
                list.append(i)
    if sum(list) == n:
            print(str(n), ' = ', ' + '.join(str(i) for i in list), sep='')
    else:
        print(str(n), 'is NOT perfect.')
