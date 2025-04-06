n = int(input())

arr = list(range(1, 101))

for i in range(len(arr)):
    if sum(arr[0:i+1]) >= n:
        print(arr[i])
        break
