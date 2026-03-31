class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Here are my thoughts

        Keep track of two indices, i and j
        If s[i] == t[j], we can start to look for numDistinct on the rest of the substring
        One more consideration here:
            s = caat and t = cat
            if s[1] is t[1], we do NOT have to traverse the path at s[1]. We could skip it and go
            to s[2] to find another distinct subsequence

        if s[i] != t[j], we should increment i

        base j is the length of its strings, we have found a distinct subsequence
        and can return 1
        What if i is at the end but not j? Return 0
        What if j reaches the end but not i? Is that even possible? Based on my conditions, it will
        not be possible:

        If s = xyz and t = w
        i will go to 3, whereas t stays at 0. 

        But wait, what if we have the following string
        s = xyzd and t = xy
        after "xy", i == 2 and j == 2

        j has reached the end but not i. Would this even count? It would! We only care about j reaching the end
        """
        num_distinct = 0
        dp = {}

        def dfs(i: int, j: int):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = 0
            if s[i] != t[j]:
                dp[(i, j)] += dfs(i + 1, j)
            if s[i] == t[j]:
                # picking means to use up a space in j
                pick = dfs(i + 1, j + 1)
                # skipping means to NOT use up a space in j
                skip = dfs(i + 1, j)
                # we always skip the char of s at i since we cannot reuse elements at i
                dp[(i, j)] += pick + skip
            return dp[(i, j)]
        
        return dfs(0, 0)
            

