class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # left <= right means keep searching while there is at least one element left
        # For example, nums[5] and target = 5, where left = right = 0
        # left < right would never trigger because 0 is not less than 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1