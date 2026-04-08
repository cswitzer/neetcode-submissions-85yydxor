class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask (to simulate fixed-size integers)
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # step 1: sum without carry
            # & mask keeps our bit as a 32 bit integer
            # Bits:  101  1101... (total 35 bits)
            # Mask:  000  1111... (total 32 ones)
            # ---------------------------
            # Result:000  1101... (The extra 3 bits are "cut" to zero)
            sum_ = (a ^ b) & mask

            # step 2: carry
            carry = ((a & b) << 1) & mask

            # step 3: update values
            # a becomes the sum, b becomes the carries waiting to be added
            a = sum_
            b = carry

        # step 4: handle negative numbers
        # ~ is mathematically defined as ~x = -(x + 1)
        return a if a <= max_int else ~(a ^ mask)
