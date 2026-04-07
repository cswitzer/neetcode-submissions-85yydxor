class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask (to simulate fixed-size integers)
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # step 1: sum without carry
            sum_ = (a ^ b) & mask

            # step 2: carry
            carry = ((a & b) << 1) & mask

            # step 3: update values
            a = sum_
            b = carry

        # step 4: handle negative numbers
        return a if a <= max_int else ~(a ^ mask)
