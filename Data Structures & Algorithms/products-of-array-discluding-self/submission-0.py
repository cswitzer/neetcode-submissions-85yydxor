class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        indices = set()
        for i, n in enumerate(nums):
            indices.add(i)

        for index, num in enumerate(nums):
            not_self = indices - set([index])
            for i in not_self:
                result[index] *= nums[i]
        
        return result
        