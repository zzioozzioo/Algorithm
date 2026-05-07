def solution(x):

    total = 0
    num_list = []

    for i in str(x):
        num_list.append(int(i))
    total = sum(num_list)

    if x%total == 0:
        answer = True
    else:
        answer = False
    
    return answer