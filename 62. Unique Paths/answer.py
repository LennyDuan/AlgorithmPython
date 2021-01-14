def uniquePaths(self, m: int, n: int) -> int:
    matrix = [[1 for _ in range(n)] for _ in range(m)]
    print(matrix)

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[-1][-1]


m = 3
n = 7
print(uniquePaths(None, m, n))
