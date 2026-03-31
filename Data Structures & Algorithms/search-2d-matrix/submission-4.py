class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        num_elements = ROWS * COLS
        left, right = 0, num_elements - 1

        while left <= right:
            mid = left + (right - left) // 2
            curr_row = mid // COLS
            curr_col = mid % COLS
            if matrix[curr_row][curr_col] == target:
                return True
            elif matrix[curr_row][curr_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False