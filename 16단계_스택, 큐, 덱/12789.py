import sys

N = int(sys.stdin.readline().rstrip())
student = []
wait = list(map(int, sys.stdin.readline().rstrip().split()))
target = 1

for i in wait:
    student.append(i)
    while student and student[-1] == target:
        student.pop()
        target += 1

    # 여긴 없어도 되는 코드인데..?
    # if len(student) > 1 and student[-1] > student[-2]:
    #     print('Sad')
    #     sys.exit()

if not student: # 모두 순서대로 나가서 student가 비었으면
    print('Nice')
else:
    print('Sad')
# 혹은 이렇게 작성해도 된다.
# print('Nice' if not Student else 'Sad')

