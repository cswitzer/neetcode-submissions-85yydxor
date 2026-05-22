class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]

        # dp[i][j] represents whether substring s[i:j+1] is a palindrome.
        #
        # A substring is a palindrome if:
        # 1. the outer characters match
        # 2. the inner substring s[i+1:j] is also a palindrome
        #
        # Therefore dp[i][j] depends on dp[i+1][j-1],
        # meaning smaller substrings must be computed before larger ones.
        #
        # We iterate i backwards so dp[i+1][j-1] is already computed
        # when evaluating dp[i][j].
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1

        return count