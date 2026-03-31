class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(i: int):
            """
            I have two choices:
            pick 1 letter or pick 2
            if letter starts with 0, return 0
            """
            if i >= len(s):
                return 1
            
            # number cannot start with a "0"
            if s[i] == "0":
                return 0
            
            if i in dp:
                return dp[i]

            pick_one = dfs(i + 1)
            
            pick_two = 0
            if (i + 1) < len(s) and int(f"{s[i]}{s[i+1]}") <= 26:
                pick_two = dfs(i + 2)
            
            dp[i] = pick_one + pick_two
            return dp[i]

        return dfs(0)        
