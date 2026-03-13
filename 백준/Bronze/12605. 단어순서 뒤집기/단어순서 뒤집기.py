import sys
input = sys.stdin.readline
N = int(input())

for case in range(1, N+1):
    words = input().split()
    words.reverse()
    print(f'Case #{case}: ', end='')
    print(*words)