avg_score = 0.0 # (학점 * 과목평점)의 총합
total = 0.0 # 학점 총합

score = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]


for i in range(20):
    a, b, c = input().split()
    b = float(b) # 문자열 b를 실수형으로 변환
    if c != 'P':
        total += b
        avg_score += b * grade[score.index(c)]

print('%.6f'%(avg_score/total))
