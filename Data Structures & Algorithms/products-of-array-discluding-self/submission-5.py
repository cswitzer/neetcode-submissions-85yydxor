class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums -> [5, 6, 7, 8]
        pref -> [1, 5, 30, 210]
        suff -> [336, 56, 8, 1]
        """
        n = len(nums)
        result = [1] * n

        # prefix is the product of everything on the left of i
        # postfix is the product of everything on the right of i
        prefix = postfix = 1

        for i in range(n):
            result[i] = prefix
            # now, compute the new prefix for i + 1
            prefix = prefix * nums[i]
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix = postfix * nums[i]
        return result
