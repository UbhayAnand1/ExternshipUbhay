def create_matrix(n):
    matrix  = [[0] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

identity_matrix = create_matrix(4)

for row in identity_matrix:
    print(row)
    
