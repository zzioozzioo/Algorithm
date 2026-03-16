car_num = input()
count = 1
for i in range(len(car_num)):
    if car_num[i] == 'c': # 문자
        case = 26
        if i > 0 and car_num[i] == car_num[i-1]:
            case -= 1
        count *= case

    elif car_num[i] == 'd': # 숫자
        case = 10
        if i > 0 and car_num[i] == car_num[i-1]:
            case -= 1
        count *= case

print(count)