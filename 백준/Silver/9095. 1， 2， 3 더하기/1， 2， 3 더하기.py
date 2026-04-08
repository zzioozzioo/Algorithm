T = int(input())

for _ in range(T):
    n = int(input())
    m = [1, 2, 4] + [0]*(n-3)
    
    for i in range(3, n):
        m[i] = m[i-1] + m[i-2] + m[i-3]
    
    print(m[n-1])