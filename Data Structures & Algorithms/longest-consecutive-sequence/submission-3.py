class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        # Worst case O(N)
        for n in nums_set:
            # is this number the start of a sequence
            if not n - 1 in nums:
                curr_len = 0
                while n + curr_len in nums_set:
                    curr_len += 1
                longest = max(longest, curr_len)
        return longest