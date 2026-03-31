class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums = sorted(nums)
        
        for i, a in enumerate(nums):
            if a > 0:
                # sorted here, so 0 is no longer possible
                break
            
            # skip duplicate values since we already checked sums for it
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum == 0:
                    sums.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # again, skip duplicate initial values we already calculated before
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
        return sums