class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n - 1] = 1

        # nums = [1, 2, 3, 4]
        # pref = [1, 1, 2, 6]
        # e.g. 3's prefix => 2 * its own prefix
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        # nums = [1, 2, 3, 4]
        # suff = [24, 12, 4, 1]
        # e.g. 2's postfix => 3 * its own postfix
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        return [prefix[i] * suffix[i] for i in range(n)]
