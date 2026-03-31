class Solution:
    def reverseBits(self, n: int) -> int:
        """
        012345
        000111
        111000

        Each element swaps positions with the element at last_i - i
        for example, in a 6 bit number

        0 <-> 5 (5 - 0)
        1 <-> 4 (5 - 1)
        2 <-> 3 (5 - 2)
        3 <-> 2 (5 - 3)
        4 <-> 1 (5 - 4)
        5 <-> 0 (5 - 5)

        Using n - i for a 32 bit number, we get the formula for 31 - i. Using this,
        we can construct the new set of bits efficiently

        We can shift either left or right, but we need to keep track of the LSB or MSB that gets cut of
        and add it to the other side. Let us shift left, save the position of the LSB, and add that to
        the position of the MSB
        """
        result = 0
        for i in range(32):
            # shift right until we get the bit at position i we care about
            # mirror the position in the result
            bit = (n >> i) & 1
            result |= bit << (31 - i)
        return result