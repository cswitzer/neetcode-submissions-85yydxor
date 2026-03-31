class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        L = 0
        max_len = 0
        win = set()

        for R in range(len(s)):
            while s[R] in win:
                win.remove(s[L])
                L += 1
            win.add(s[R])
            max_len = max(len(win), max_len)
                
        
        return max_len
