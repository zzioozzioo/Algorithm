import sys
input = sys.stdin.readline

N = int(input())

points = []
for _ in range(N):
    num = tuple(map(int, input().split()))
    points.append(num)

points.sort(key=lambda x: (x[1], x[0]))
for point in points:
    print(' '.join(map(str, point)))