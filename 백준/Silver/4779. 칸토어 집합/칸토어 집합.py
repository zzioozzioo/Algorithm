def getCantor(size):
    # base condition
    if size == 1: return '-'

    # divide
    new_size = size // 3
    center = ' ' * new_size
    side = getCantor(new_size)
    return side + center + side

while True:
    try:
        N = int(input())
        size = 3**N
        result_str = getCantor(size)
        print(result_str)
    except EOFError:
        break