class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            curr_longest = 1
            n_copy = n
            while n_copy - 1 in nums_set:
                curr_longest += 1
                n_copy -= 1
            longest = max(longest, curr_longest)
        return longest