def solution(my_string, is_prefix):
    answer = 0
    prefix = []

    for i in range(len(my_string)):
        prefix.append(my_string[0:i + 1])

    if is_prefix in prefix:
        answer = 1

    return answer