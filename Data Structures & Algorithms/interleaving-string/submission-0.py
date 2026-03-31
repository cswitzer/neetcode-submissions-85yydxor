class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        if k is the len of s3, we confirmed that s3 is s1 and s2 interleaving
        only traverse s1 if i < len s1 and s1[i] == s3[k]
        only traverse s2 if j < len s2 and s2[j] == s3[k]

        The state of each rec call is (i, j, k)
        """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i: int, j: int, k: int):
            if k == len(s3):
                return True
            if i < len(s1) and j < len(s2) and s1[i] != s3[k] and s2[j] != s3[k]:
                return False
            if (i, j, k) in dp:
                return dp[(i, j, k)]

            take_s1 = False
            take_s2 = False
            if i < len(s1) and s1[i] == s3[k]:
                take_s1 = dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                take_s2 = dfs(i, j + 1, k + 1)
            dp[(i, j, k)] = take_s1 or take_s2
            return dp[(i, j, k)]

        return dfs(0, 0, 0)

