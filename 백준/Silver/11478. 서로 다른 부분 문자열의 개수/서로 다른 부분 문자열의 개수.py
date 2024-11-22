import sys
input = sys.stdin.readline

S = input().strip()
set = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        set.add(S[i:j+1]) # i 인덱스에서 (j+1)-1 인덱스까지 슬라이싱

print(len(set))