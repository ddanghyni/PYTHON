matrix = [] 
nrow = 3
ncol = 3
for _ in range(ncol):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)

new_matrix = []

for i in range(nrow):
    new_row = []
    for j in range(ncol):
        new_row.append(matrix[i][j] * 3)
    new_matrix.append(new_row)

for i in range(nrow):
    for j in range(ncol):
        print(new_matrix[i][j], end = " ")
    print()
