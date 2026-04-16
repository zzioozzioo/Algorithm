N, M = map(int, input().split())

int_key = {} 
name_key = {}

for i in range(1, N+1):
    data = input().strip()
    int_key[i] = data
    name_key[data] = i

for _ in range(M):
    data = input().strip()

    if data.isdigit() == True:
        print(int_key[int(data)])
    else:
        print(name_key[data])