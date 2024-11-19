import math
import sys

input = sys.stdin.readline

N = int(input().strip())
tree = []
count = 0

for i in range(N):
    tree.append(int(input().strip()))

# 나무 간 거리 차이 구하기
list = []
for i in range(len(tree)-1):
    list.append(tree[i+1]-tree[i])

# 최대공약수 구하기
gcd = list[0]
for i in range(1, len(list)):
    gcd = math.gcd(gcd, list[i])

for i in list:
    count += (i//gcd) -1

print(count)