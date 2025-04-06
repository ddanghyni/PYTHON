n = int(input())

arr = list(range(1, 101))

for i in range(len(arr)):
    if sum(arr[1:i+2]) >= n:
        print(arr[i+1])
        break
