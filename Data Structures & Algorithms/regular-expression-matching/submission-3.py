class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        p is the pattern, s is the string
        p consists of lowercase english characters, ".", and "*"

        "." matches any single character
        "*" matches 0 or more of the preceding element

        Case 1
        So this would mean:
        s = abbb
        p = .b*
        This is a pattern match because
        
        "." => a
        "b*" => bbb

        Case 2
        xyz and ".*z"
        .* matches x & y, while z matches z

        Case 3
        s = "" and p = n*
        matches because n* matches ZERO or more
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


