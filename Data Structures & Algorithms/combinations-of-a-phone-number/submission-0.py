class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        curr = []
        char_nums_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i: int):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return
            for c in char_nums_map[digits[i]]:
                curr.append(c)
                backtrack(i + 1)
                curr.pop()
        
        if digits:
            backtrack(0)
        
        return result
            
