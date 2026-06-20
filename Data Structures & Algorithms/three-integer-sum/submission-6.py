class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # if i is the same value as the previous, the triplet will be duplicated
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
        return result
