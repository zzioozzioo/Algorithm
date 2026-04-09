import sys
input = sys.stdin.readline

N = int(input())

points = list(map(int, input().split()))
zip = sorted(set(points))

dic = {}
for i in range(len(zip)):
    num = zip[i]
    order = i
    dic[num] = order

for i in points:
    print(dic[i], end=' ')