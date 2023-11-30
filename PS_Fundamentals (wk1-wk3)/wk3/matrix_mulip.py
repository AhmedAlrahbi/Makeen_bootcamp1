matrix = [[1,2,3],
          [6,7,8]]

matrix1 = [[6,1],
           [2,10],
           [0,2]]
result = [[0,0],[0,0]]

for i in range(0, len(matrix)):
    for j in range (0, len(matrix1[i])):
        for k in range(0, len(matrix1)):
            result[i][j] += matrix[i][k] * matrix1[k][j]
for row in result:
    print(row)








