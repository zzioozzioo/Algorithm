import sys
input = sys.stdin.readline
gcd = 0

T = int(input().strip())
for _ in range(T):
    A, B = map(int, input().strip().split())
    for i in range(max(A, B), 0, -1):
        if A%i==0 and B%i==0:
            gcd = i
            break
    print(int((A*B)/gcd))