class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 2
        (())
        ()()
        """
        parans = []
        cand = []

        def backtrack(num_open: int = 0, num_closed: int = 0):
            if num_open == n and num_closed == n:
                parans.append("".join(cand[:]))
                return

            # add "("
            if num_open < n:
                cand.append("(")
                backtrack(num_open + 1, num_closed)
                cand.pop()

            # invalid, we cannot have something like ')', '())', or ')('
            if num_closed < num_open and num_closed < n:
                cand.append(")")
                backtrack(num_open, num_closed + 1)
                cand.pop()

        backtrack()
        return parans