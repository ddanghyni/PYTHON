n = int(input()) #len(arr)

arr = list(map(int, input().split()))

ans = []

for x in arr:
    if x % 2 == 0:
        ans.append(x)
    else:
        pass

ans.reverse()

for x in ans:
    print(x, end = " ")