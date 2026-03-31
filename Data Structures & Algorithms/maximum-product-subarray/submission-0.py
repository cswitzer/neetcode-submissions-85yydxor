class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1

        for num in nums:
            temp = num * curr_max

            # if "curr_min" and "num" are negative, it could be a new max
            # [-1, -100, 1000] we mean "num" is the new max since 1,000 > 100
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(temp, curr_min * num, num)
            res = max(res, curr_max)
        return res