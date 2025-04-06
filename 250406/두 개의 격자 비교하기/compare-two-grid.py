row, col = map(int, input().split())

mat = []
for _ in range(row * 2):
    data_row = list(map(int, input().split()))
    mat.append(data_row)
    
ans_mat = []

for i in range(row):
    ans_mat.append([1] * col) 
        
for i in range(row):
    for j in range(col):
        if mat[i][j] == mat[i + row][j]:
            ans_mat[i][j] = 0

for i in range(row):
    for j in range(col):
        print(ans_mat[i][j], end= " ")
    print()