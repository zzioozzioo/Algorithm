import sys

input = sys.stdin.readline

N = int(input().rstrip())
num_list = list(map(int, input().rstrip().split()))
print(max(num_list)*min(num_list))