class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix:
            return 0
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < rows - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < cols - 1 and val > matrix[i][j + 1] else 0)

            return dp[i][j]

        for row in range(rows):
            for col in range(cols):
                res = max(dfs(row, col), res)

        return res


nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print(longestIncreasingPath(None, nums))
