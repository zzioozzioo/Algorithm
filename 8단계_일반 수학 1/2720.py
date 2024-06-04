T = int(input())
Q, D, N, P = 0, 0, 0, 0

for i in range(T):
    C = int(input())

    Q = C // 25
    C %= 25

    D = C // 10
    C %= 10

    N = C // 5
    C %= 5

    P = C // 1
    C %= 1
    
    print(int(Q), int(D), int(N), int(P))
