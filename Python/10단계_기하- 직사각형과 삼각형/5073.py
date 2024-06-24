while True:
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        if max(a, b, c) >= (a+b+c-max(a,b,c)):
            print('Invalid')
        else:
            if a==b and a==c and b==c:
                print('Equilateral')
            elif a!=b and b!=c and a!=c:
                print('Scalene')
            else:
                print('Isosceles')