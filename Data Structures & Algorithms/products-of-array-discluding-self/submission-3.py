class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums -> [1, 2, 3, 4]
        pref -> [1, 1, 2, 6] (6 comes from everything to the left of 4)
        suff -> [24, 12, 4, 1] (24 comes from everything to the right of 1)
        """
        size = len(nums)

        result = []
        pref = [1 for _ in range(size)]
        suff = [1 for _ in range(size)]

        for i in range(1, size):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(size - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(size):
            result.append(pref[i] * suff[i])
        
        return result