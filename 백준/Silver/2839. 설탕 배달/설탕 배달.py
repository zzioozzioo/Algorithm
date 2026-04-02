N = int(input())
num_list = []
# five, three = 0, 0

# five = N//5
# three = (N-five*5)//3 # 혹은 N%5도 가능
# if five*5+three*3 != N:
#     if N%3 == 0:
#         three = N//3
#         print(three)
#     else:        
#         print(-1)
# else:
#     print(five+three)
for i in range(N):
    for j in range(N):
        if 5*i+3*j == N:
            num_list.append(i+j)
if len(num_list) != 0:
    print(min(num_list))
else:
    print(-1)
