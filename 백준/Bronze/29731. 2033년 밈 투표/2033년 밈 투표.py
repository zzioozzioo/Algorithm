promise = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

n = int(input())
check_num = n

for i in range(n):
    p = input()
    if p not in promise:
        n -= 1
        break

if check_num == n:
    print("No")
else:
    print("Yes")