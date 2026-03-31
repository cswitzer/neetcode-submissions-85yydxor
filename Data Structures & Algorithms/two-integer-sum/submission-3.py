class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if num in complements:
                return [complements[num], i]
            complements[diff] = i