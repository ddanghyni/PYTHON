n = int(input())

counter = 0

for i in range(1, n + 1):
    cond = (i % 2 == 0) | (i % 3 == 0) |(i % 5 == 0)
    if cond:
        counter += 1

print(len(range(1, n+1)) - counter)

