from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def is_yellow(signal, t):
    G, Y, R = signal
    cycle = G + Y + R
    pos = (t - 1) % cycle
    return G <= pos < G + Y

def solution(signals):
    # 1) 전체 반복 주기 구하기
    total_cycle = 1
    for G, Y, R in signals:
        cycle = G + Y + R
        total_cycle = lcm(total_cycle, cycle)

    # 2) 1초부터 전체 반복 주기까지 검사
    for t in range(1, total_cycle + 1):
        if all(is_yellow(signal, t) for signal in signals):
            return t

    # 3) 끝까지 없으면 불가능
    return -1