class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0

        left = 0
        for right, c in enumerate(s):
            while c in seen and left < right:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            longest = max(longest, (right - left) + 1)

        return longest