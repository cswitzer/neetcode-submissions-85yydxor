class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        neetcode
        dict = [neet, code]
        true - neetcode can be split into neet and code

        n
        dict[0] starts with n
        s[0:len(neet)] is in dict
        continue from c onwards
        c
        dict[1] starts with c
        s[4:len(code)] is in dict
        continue from len(s) onwards
        now at len(s)
        return True

        However, what if s = neetcodes, [neet, code, super]
        We would start at s which is index 9
        if nothing starts with s in wordDict, we return false
        we have super, but it does not exist in s, so we return False
        """
        memo = { len(s): True }

        def dfs(i: int):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i:len(w) + i] == w):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            
            # means the string cannot be segmented starting from this index
            memo[i] = False
            return False
        
        return dfs(0)

