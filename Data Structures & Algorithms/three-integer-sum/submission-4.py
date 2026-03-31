class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        sorted_nums = sorted(nums)

        for i in range(n - 2):
            # dup first values result in dupl results, so skip dup first values
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if curr_sum == 0:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        return result
