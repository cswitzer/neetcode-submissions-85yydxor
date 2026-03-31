class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # each number is 1 <= v <= n
        # the len of the array is n + 1
        # this means for every number, abs(num) - 1 is always a valid index
        # this means that for every number, if the index at abs(num) - 1 is already negative, we found a duplicate

        # [1, 4, 3, 1]
        # 1st it [-1, 4, 3, 1]
        # 2nd it [-1, 4, 3, -1]
        # 3rd it [-1, 4, -3, -1]
        # 4th it 1 is the duplicate since nums[abs(-1) - 1] => nums[0] => -1 is less than 0, so we found the duplicate
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1