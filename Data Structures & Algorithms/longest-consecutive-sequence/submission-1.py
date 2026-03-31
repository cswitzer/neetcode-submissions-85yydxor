class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # Is this the start of a sequence?
            if not num - 1 in nums_set:
                length = 0
                # As long as consecutive nums exist in the set...
                while num + length in nums_set:
                    length += 1
                longest = max(longest, length)
        
        return longest