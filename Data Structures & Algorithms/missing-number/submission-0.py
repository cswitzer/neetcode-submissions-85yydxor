class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Only ONE number is missing.

        XOR is associative and commutative, and a ^ a = 0.

        If we XOR all numbers in nums with all numbers from 0 to n,
        every number cancels out except the missing one.

        Example:
        nums = [0,2,3,4,5]
        full = [0,1,2,3,4,5]

        All matching numbers cancel, leaving 1.
        """
        n = len(nums) # handle n here, which is 5 in "full" above
        xorr = n 
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr