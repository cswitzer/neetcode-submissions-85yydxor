class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(i: int, num_open: int, num_closed: int):
            if (i, num_open, num_closed) in dp:
                return dp[(i, num_open, num_closed)]
            if num_closed > num_open:
                return False
            
            # The condition that tells us if the string is valid
            if i == len(s):
                if num_open == num_closed:
                    return True
                return False                

            is_valid = False
            if s[i] == "(":
                is_valid = dfs(i + 1, num_open + 1, num_closed)
            elif s[i] == ")":
                is_valid = dfs(i + 1, num_open, num_closed + 1)
            else:
                is_valid = (
                    dfs(i + 1, num_open + 1, num_closed) or
                    dfs(i + 1, num_open, num_closed + 1) or
                    dfs(i + 1, num_open, num_closed)
                )
            dp[(i, num_open, num_closed)] = is_valid
            return dp[(i, num_open, num_closed)]
        
        return dfs(0, 0, 0)