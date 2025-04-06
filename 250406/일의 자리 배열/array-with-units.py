ary = list(map(int, input().split()))

ans = []

ans.append(ary[0])
ans.append(ary[1])

i = 0
j = 1
while len(ans) < 10:
    ans.append((ans[i] + ans[j]) % 10)
    i += 1
    j += 1

for x in ans:
    print(x, end = " ")


