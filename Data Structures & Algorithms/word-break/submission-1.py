class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i:i + len(w)] == w):
                    # e.g. for s = code and wordDict = [code]
                    # then memo[4] = True, which means memo[0] = memo[4] = True
                    # another is neetcode and [neet, code] where
                    # dp[8] = True, dp[4] = True, and therefore dp[0] = True
                    memo[i] = memo[i + len(w)]
                if memo[i]:
                    break
        
        return memo[0]
