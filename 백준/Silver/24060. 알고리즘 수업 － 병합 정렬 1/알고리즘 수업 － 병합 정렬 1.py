import sys

input = sys.stdin.readline

def merge_sort(A, p, r): # A[p ~ r]을 오름차순 정렬한다.
  if p < r:
    q = (p + r) // 2; # q는 p, r의 중간 지점
    merge_sort(A, p, q)       # 전반부 정렬
    merge_sort(A, q+1, r)   # 후반부 정렬
    merge(A, p, q, r)

def merge(A, p, q, r):
    global count, value
    i = p
    j = q+1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
       tmp.append(A[i])
       i += 1
    while j <= r:
       tmp.append(A[j])
       j += 1

    i = p
    t = 0
    
    while i <= r:
       A[i] = tmp[t]
       count += 1
       if count == K:
           value = A[i]
           break
       i += 1
       t += 1
           
N, K = map(int, input().rstrip().split())

A = list(map(int, input().rstrip().split()))

count, value = 0, -1
merge_sort(A, 0, N-1)
print(value)