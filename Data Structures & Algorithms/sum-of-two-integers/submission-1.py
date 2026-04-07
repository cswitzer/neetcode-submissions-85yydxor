class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        both are 32 bit integers

        We need two values, the sum and the carry
        0 + 0 => sum 0 and carry 0
        1 + 0 => sum 1 and carry 0
        1 + 1 => sum 0 and carry 1

        When carry is 1, we add it to the next set of bits
        Sum   => a[i] ^ b[i]
        Carry => a[i] & b[i]
        """
        carry = 0
        res = 0

        for i in range(32):
            # get the ith bit's value
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            # get the sum of the current column without the carry
            # so 0 0 0 is 0 carry 0
            # 1 0 0 is 1 carry 0
            # 1 1 0 is 0 carry 1
            # 1 1 1 is 0 carry 1
            cur_bit = a_bit ^ b_bit ^ carry

            # do we have a carry?
            carry = (a_bit + b_bit + carry) >= 2

            # add the bit to the ith/current position in result
            if cur_bit:
                res |= (1 << i)
            
        # if result is too large, the number must be negative
        # this is because in 32-bit signed integers, the MSB represents the sign!
        # if python goes beyond 01111111111111111111111111111111, then the MSB must be 1
        # and that represents a negative
        if res > 0x7FFFFFFF: # or 0b01111111111111111111111111111111
            res -= 1 << 32

        return res
