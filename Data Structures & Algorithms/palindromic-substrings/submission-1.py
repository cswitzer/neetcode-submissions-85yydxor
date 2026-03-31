class Solution:
    def countSubstrings(self, s: str) -> int:
        n, count = len(s), 0

        # cache whether s from l to j is a palindrome
        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l + 1 <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    count += 1
        
        return count
