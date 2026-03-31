class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        ((**)
        left_min = -1
        left_max = 3

        2 open
        1 closed
        2 stars
        """
        left_min = 0
        left_max = 0
        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            
            # If the max possible number of left open is negative, we know that
            # we do not have enough opening parans
            if left_max < 0:
                return False
            
            # The left min being less than 0 could be due to "*" chars, which can also
            # be treated as empty spaces
            if left_min < 0:
                left_min = 0
            
        return left_min == 0
        