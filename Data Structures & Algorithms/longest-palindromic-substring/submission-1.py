class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_index, res_len = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if res_len < (r - l + 1):
                        res_index = l
                        res_len = (r - l + 1)
        
        return s[res_index : res_index + res_len]