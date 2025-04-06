n = int(input())
tmp = 1
for i in range(1, n + 1):
    for j in range(tmp):
        print("*", end="")
    tmp+=2
    print()
