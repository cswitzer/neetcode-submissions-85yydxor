class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x:
            digit = x % 10
            x //= 10
            result = result * 10 + digit

        result *= sign

        if result < MIN or result > MAX:
            return 0

        return result
