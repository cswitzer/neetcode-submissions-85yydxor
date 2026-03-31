class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        present_chars = set()
        for right in range(len(s)):
            while s[right] in present_chars:
                present_chars.remove(s[left])
                left += 1
            present_chars.add(s[right])
            max_len = max(max_len, len(present_chars))
        return max_len