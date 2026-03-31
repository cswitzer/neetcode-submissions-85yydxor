class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for idx, num in enumerate(nums):
            indices[num] = idx
        
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in indices and idx != indices[complement]:
                return [idx, indices[complement]]
        