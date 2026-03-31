class Solution:
    def hammingWeight(self, n: int) -> int:
        # in python, an int is 32 bits, so we loop 32 times
        # we can right shift the bits after counting, taking into account the
        # number of 1's we encounter
        weight = 0
        for _ in range(32):
            if n & 1 == 1:
                weight += 1
            n >>= 1
        return weight