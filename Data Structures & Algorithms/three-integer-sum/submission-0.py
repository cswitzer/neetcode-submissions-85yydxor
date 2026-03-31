class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        sorted_nums = sorted(nums)

        for i in range(n - 2):
            # dup first values result in dupl results, so skip dup first values
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            curr_num = sorted_nums[i]
            left, right = i + 1, n - 1
            while left < right:
                three_sum = curr_num + sorted_nums[left] + sorted_nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                   result.append([curr_num, sorted_nums[left], sorted_nums[right]])
                   left += 1
                   while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
        return result
