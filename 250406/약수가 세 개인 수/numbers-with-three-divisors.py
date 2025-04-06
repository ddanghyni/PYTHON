start, end = map(int, input().split())
ans = 0
# Please write your code here.
for i in range(start, end + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter == 3:
        ans += 1
print(ans)