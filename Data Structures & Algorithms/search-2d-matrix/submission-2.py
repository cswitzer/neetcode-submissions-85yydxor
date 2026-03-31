class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row: List[int], target: int):
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (low + high) // 2

                if row[mid] < target:
                    low = mid + 1
                elif row[mid] > target:
                    high = mid - 1
                else:
                    return True
            
            return False
        
        for row in matrix:
            if binary_search(row, target):
                return True
        
        return False