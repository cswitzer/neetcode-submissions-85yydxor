class Solution:
    def _fast_pow(self, x: float, n: int) -> float:
        """
        break exponent in half each time for O(log(n)) time
        So fast_pow(2.00, 8) would be 2 ** 8

        So 2 ** 8 == (2 ** 4) * (2 ** 4)
        2 ** 4 == (2 ** 2) * (2 ** 2)
        2 ** 2 == (2 ** 1) * (2 ** 1)
        2 ** 1 == (2 ** 0) * (2 ** 0) [Base case]

        What about odd numbers?
        2 ** 5
        Since 5 is odd, we peel off an exponent like this to make the numbers even

        - 2 * (2 ** 4), which will be expressed recursively as 2 * (2 ** 2) ** 2

        For negatives, remember the identity x ** -n == 1 / x ** n
        """
        if n == 0:
            return 1

        half = self._fast_pow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            # peel off 1 exponent to compute an even amount
            return half * half * x

    def myPow(self, x: float, n: int) -> float:
        """
        x to the power of n.
        """
        res = self._fast_pow(x, abs(n))
        return res if n >= 0 else 1 / res
