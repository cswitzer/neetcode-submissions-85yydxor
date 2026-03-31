class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        In a nutshell, the algorithm does this:

        1. Check if chars match
        2. If next char is *
            Skip star or use star
        3. Else
            Move both pointers
        """
        dp = {}

        def dfs(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            # case s = aa and j = a means no match
            if j >= len(p):
                return False
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            # case s = a and j = a*b* -> Just because i is out of bounds but not j, it does not mean
            # p does not match i
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                # either take the star or do not take the star
                # we can only take a star if s[i] == p[j]
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)


