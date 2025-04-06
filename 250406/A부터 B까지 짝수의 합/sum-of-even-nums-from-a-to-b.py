A, B = map(int, input().split())

ans = 0

for i in range(A, B+1):
    if i % 2 == 0:
        ans += i
print(ans)