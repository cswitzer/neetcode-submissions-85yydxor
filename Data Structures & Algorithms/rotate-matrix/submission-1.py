class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        matrix is n x n, so this is a square

        1 2 3         7 4 1
        4 5 6 BECOMES 8 5 2
        7 8 9         9 6 3

        REVERSE
        
        7 8 9
        4 5 6
        1 2 3

        TRANSPOSE
        """
        # Reverse matrix vertically
        matrix.reverse()

        # Transpose the matrix
        for r in range(len(matrix)):
            # r + 1 so we only process the top triangle of the diagonal
            for c in range(r + 1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
