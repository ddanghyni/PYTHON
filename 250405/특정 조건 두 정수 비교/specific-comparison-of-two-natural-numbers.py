first, second = map(int, input().split())

if first < second:
    ans_1 = 1
else:
    ans_1 = 0

if first == second:
    ans_2 = 1
else:
    ans_2 = 0

print(ans_1, ans_2)

