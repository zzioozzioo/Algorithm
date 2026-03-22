S = input()
length = len(S)
stack = []

i=0
while i < length:
    # 공백이거나 '<'이 아닌 경우(일반 문자열)
    if S[i] not in [' ', '<']: 
        stack.append(S[i]) # 그냥 스택에 쌓기
        i += 1

    # 공백 or '<'
    else: 
        # 그 전 문자열 거꾸로 출력
        while stack:
            print(stack.pop(), end = '') 

        # '<'인 경우 처리
        if S[i] == '<':
            while S[i] != '>':
                print(S[i], end = '')
                i += 1
            print('>', end='')
            i += 1
            
        # 공백인 경우 처리
        else:
            print(' ', end='')
            i += 1


while stack:
    print(stack.pop(), end = '')