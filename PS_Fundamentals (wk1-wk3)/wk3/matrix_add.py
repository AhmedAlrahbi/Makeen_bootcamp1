#ICA, 26112023, matrix additon
counter = 0
matrix2 = []
row =[]
matrix = [[0,5,1],
          [4,9,0],
          [0,6,0]]
matrix1 = [[5, 5, 1],
           [5,8,1],
           [9,2,6]]
eleRes = []
x=[]
for i in range (len(matrix)):
    eleRes.append([0]*len(matrix))
    for j in range (len (matrix[0])):
        eleRes[i][j] = matrix [i][j] + matrix1[i][j]
for r in eleRes:
    x.append(r)
print (x)
#         if (matrix[i][j] == 0):
#             counter+=1
# print(counter)
