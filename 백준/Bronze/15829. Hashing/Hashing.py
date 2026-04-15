M = 1234567891
r = 31

L = int(input())
A = input().strip()

h = 0
for i in range(L):
    # a:1, b:2, ... -> ord(A[i]) - ord('a') + 1
    # a값 * r**i%M
    h += (ord(A[i]) - ord('a') + 1) * r**i

print(h%M)