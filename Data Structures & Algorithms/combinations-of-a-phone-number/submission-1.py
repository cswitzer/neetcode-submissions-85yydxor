class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        input: 23
        output = ad, ae, af, bd, be, bf, cd, ce, cf
        """
        result = []
        if not digits:
            return result

        combination = []
        num_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int = 0):
            if index == len(digits):
                result.append("".join(combination[:]))
                return

            digit = digits[index]
            for char in num_letter_map[digit]:
                combination.append(char)
                backtrack(index + 1)
                combination.pop()

        backtrack()
        return result
