N = int(input())
a_points = []
b_points = []
a, b = 0, 0

for _ in range(N):
    a, b = map(int, input().split())
    a_points.append(a)
    b_points.append(b)
    
a = max(a_points)-min(a_points)
b = max(b_points)-min(b_points)
print(a * b)
