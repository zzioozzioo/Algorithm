N, M = map(int, input().split())
card_list = [int(card) for card in input().split()]

def findMax():
    max = 0
    for card1_index in range(N-2):
        for card2_index in range(card1_index+1, N-1):
            for card3_index in range(card2_index+1, N):
                sum = card_list[card1_index] + card_list[card2_index] + card_list[card3_index]
                if sum == M: return sum
                elif max < sum < M: max = sum
    return max

print(findMax())                