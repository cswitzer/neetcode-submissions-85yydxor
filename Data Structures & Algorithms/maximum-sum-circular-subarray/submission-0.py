class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for num in nums:
            # [5, -3, 5]
            curr_max = max(curr_max + num, num) # take 5 + -3 + 5 OR just 5
            curr_min = min(curr_min + num, num) # take 5 + -3 OR just take -3
            total += num
            glob_max = max(glob_max, curr_max)
            glob_min = min(glob_min, curr_min)
        
        # edge case: glob_max < 0 means the array has ALL negatives
        return max(total - glob_min, glob_max) if glob_max > 0 else glob_max