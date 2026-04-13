N, S = map(int, input().split())
num_list = list(map(int, input().split()))

count = 0

def solve(index, currentSum):
    global count

    if index == N:
        if currentSum == S:
            count += 1
        return
    
    solve(index + 1, currentSum + num_list[index])
    solve(index + 1, currentSum)

solve(0, 0)

if S == 0:
    count -= 1

print(count)