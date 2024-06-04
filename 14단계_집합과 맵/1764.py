import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
a = set()
for i in range(N):
    a.add(input().strip())

b = set()
for i in range(M):
    b.add(input().strip())

result = sorted(list(a&b))

print(len(result))

for i in result:
    print(i)
