arr = [int(input()) for _ in range(10)]

times_3 = 0
times_5 = 0

for i in arr:
    if i % 15 == 0:
        times_3 += 1
        times_5 += 1
    elif i % 5 == 0:
        times_5 += 1
    elif i % 3 == 0:
        times_3 += 1
    else:
        None
print(times_3, times_5)