N = int(input())
num = 666
index = 0
while True:
    if '666' in str(num):
        index += 1
    num += 1
    if N == index:
        print(num-1)
        break