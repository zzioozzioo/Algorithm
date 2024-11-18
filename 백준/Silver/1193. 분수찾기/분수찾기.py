X = int(input())
line = 1 # 첫 번째 분수의 값이 1/1이므로 1로 설정

while X > line:
    X -= line
    line += 1

# 짝수 번째 라인: 분자 오름차순 / 분모 내림차순
# 홀수 번째 라인: 분자 내림차순 / 분모 오름차순
if line%2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')