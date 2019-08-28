"""
CTCI - 1.7
Rotate Matrix: 
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place? 
I: nxn matrix
O: rotated matrix - 90 deg, clockwise
C: rotate matrix in place, optimize
E: empty matrix, even and odd values for n
"""

def rotatMatrix(m):
    n = len(m)
    row = n //2
    for i in range(row+1):
        for j in range(n-2*i-1):
            t = m[i+j][n-1-i]
            m[i+j][n-1-i] = m[i][i+j]
            m[i][i+j] = t

            t = m[n-1-i][n-1-i-j] 
            m[n-1-i][n-1-i-j] = m[i][i+j]
            m[i][i+j] = t

            t = m[n-1-i-j][i]
            m[n-1-i-j][i] = m[i][i+j]
            m[i][i+j] = t
    return m
def rotatMatrix2(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

m = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
print(rotatMatrix(m))
print(rotatMatrix2(m))
"""
[
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
"""

