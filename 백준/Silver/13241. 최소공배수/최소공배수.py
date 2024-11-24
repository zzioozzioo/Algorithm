import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
gcd = 0

for i in range(max(A, B), 0, -1):
    if A%i==0 and B%i==0:
        gcd = i
        break

print(int((A*B)/gcd))