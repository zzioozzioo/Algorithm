def solution(cards1, cards2, goal):
    answer = 'Yes'
    for word in goal:
        if len(cards1) and cards1[0] == word:
            del cards1[0]
        elif len(cards2) and cards2[0] == word:
            del cards2[0]
        else:
            answer = "No"
            break
    return answer