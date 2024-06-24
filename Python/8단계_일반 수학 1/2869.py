import math

A, B, V = map(int, input().split()) 
# 낮에 A미터 올라감 / 밤에 B미터 미끄러짐 / 나무 막대 높이 V미터

day = (V-B) / (A-B) 
# 도달하는 날 day / 올라가는 횟수 day번 / 내려오는 횟수 (day-1)번
# A*day - B(day-1) = V

print(math.ceil(day))