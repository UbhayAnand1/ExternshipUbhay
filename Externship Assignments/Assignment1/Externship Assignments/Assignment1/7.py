matrix = []
counter = 1

for i in range(3):
    row = []
    for j in range(3):
        row.append(counter)
        counter += 1
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)
