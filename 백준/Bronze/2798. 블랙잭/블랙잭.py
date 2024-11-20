N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
n_list = []
sum = 0

for i in range(N-2): # N-1인 이유: k의 최대가 N이니까 j의 최대는 N-1, i의 최대는 N-2이 되어야 최대가 됐을 때 수들이 겹치지 않는다. 
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = num_list[i] + num_list[j] + num_list[k]
            if sum > M:
                continue
            else:
                n_list.append(sum)

print(max(n_list))