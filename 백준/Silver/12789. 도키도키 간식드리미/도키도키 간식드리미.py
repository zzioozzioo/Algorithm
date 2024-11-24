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
   

if not student: # 모두 순서대로 나가서 student가 비었으면
    print('Nice')
else:
    print('Sad')
