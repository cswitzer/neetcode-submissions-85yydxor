class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums -> [1, 2, 3, 4]
        pref -> [1, 1, 2, 6] (6 comes from everything to the left of 4)
        suff -> [24, 12, 4, 1] (24 comes from everything to the right of 1)
        """
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        return [num1 * num2 for num1, num2 in zip(prefix, suffix)]

