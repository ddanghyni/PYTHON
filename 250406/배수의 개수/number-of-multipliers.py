arr = [int(input()) for _ in range(10)]

times_3 = 0
times_5 = 0

for i in arr:
    if i % 3 == 0:
        times_3 += 1
    if i % 5 == 0:
        times_5 += 1

print(times_3, times_5