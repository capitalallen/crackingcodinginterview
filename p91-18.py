def zeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = []
    col = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.append(i)
                col.append(j)
    for i in rows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for i in col:
        for j in range(len(matrix)):
            matrix[j][i] = 0
    return matrix

data = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
print(zeroMatrix(data))

"""
[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ]
"""
        