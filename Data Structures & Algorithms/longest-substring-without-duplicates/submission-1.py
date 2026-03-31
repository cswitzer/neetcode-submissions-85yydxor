class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            # keep popping until the character at the right is no
            # longer in seen, which marks the start of a new substr
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, len(seen))
        return max_len