# Creating two 2-dimensional arrays
array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

array2 = [[9, 8, 7],
          [6, 5, 4],
          [3, 2, 1]]

# Performing element-wise addition
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(array1)):
    for j in range(len(array1[0])):
        result[i][j] = array1[i][j] + array2[i][j]

# Printing the result
for row in result:
    print(row)
