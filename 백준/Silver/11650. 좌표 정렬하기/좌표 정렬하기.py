import sys
input = sys.stdin.readline

N = int(input())

points = []
for _ in range(N):
    num = tuple(map(int, input().split()))
    points.append(num)

# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
points.sort()
# key=lambda x: (x[0], x[1])

for point in points:
    print(' '.join(map(str, point)))