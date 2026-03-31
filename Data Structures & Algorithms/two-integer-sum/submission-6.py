class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_sums = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prev_sums:
                return [prev_sums[diff], idx]
            prev_sums[num] = idx