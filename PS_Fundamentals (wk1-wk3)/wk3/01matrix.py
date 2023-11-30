#01 matrix
numRows = int(input("Enter number of row/col: "))

matrix = []

for i in range (numRows):
    matrix.append([0]*numRows)
    for j in range (numRows):
        if (i<=j):
            matrix[i][j]= 1

print(matrix)

