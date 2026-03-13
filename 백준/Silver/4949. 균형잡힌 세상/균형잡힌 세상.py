while True:
    str = input()
    stack = []
    if str == ".": # 입력 종료조건
        break

    isGoodWord = 'yes'

    for word in str: # 스택에 괄호만 분리
        if word in ['[', '(']: # 여는 괄호인 경우
            stack.append(word)
        
        elif word == ']':
            if not stack or stack.pop() != '[':
                isGoodWord = 'no'
                break

        elif word == ')':
            if not stack or stack.pop() != '(':
                isGoodWord = 'no'
                break

    if stack:
        isGoodWord = 'no'
    
    print(isGoodWord)
          
