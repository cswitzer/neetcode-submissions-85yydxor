class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        # break the ordered 2D array into a 1D-like array
        low, high = 0, (rows * cols - 1)

        while low <= high:
            middle = (low + high) // 2
            # map 1D index to 2D index
            row, col = divmod(middle, cols)
            middle_val = matrix[row][col]

            if middle_val == target:
                return True
            elif middle_val < target:
                low = middle + 1
            else:
                high = middle - 1
        
        return False