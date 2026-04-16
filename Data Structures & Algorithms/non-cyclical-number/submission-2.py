class Solution:
    def sum_digits_squares(self, num: int):
        result = 0
        while num > 0:
            digit = num % 10
            result += digit ** 2
            num //= 10
        return result

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            n = self.sum_digits_squares(n)
            if n in seen:
                return False
        return True