class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3, 4, 5, 6, 1, 2]
        len: 6
        if mid [6 in this case] is greater than nums[-1], then the min is further right 

        [1, 2, 3, 4, 5, 6]
        if mid [4 in this case] is less than nums[-1], then the mid is further left
        len: 6

        [4, 5, 0, 1, 2, 3]

        """
        def is_further_right(mid: int) -> bool:
            return nums[mid] > nums[-1]

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if is_further_right(mid):
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]