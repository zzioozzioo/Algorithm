def solution(wallet, bill):
    answer = 0
    
    # 종료조건 어느 한쪽이 지갑보다 큰 경우에는 무한 반복
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        
        # 더 큰쪽 찾아서 접기
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        
        # 정답 +1
        answer += 1
        
    return answer