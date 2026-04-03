mushrooms = []
for _ in range(10):
    mushrooms.append(int(input()))

sum = 0
for mushroom in mushrooms:
    before = abs(sum-100)
    after = abs(sum+mushroom-100)

    if before >= after:
        sum += mushroom
    else: break

print(sum)