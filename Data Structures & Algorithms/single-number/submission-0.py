class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR has two properties:

        A number XOR'd by itself is 0
        XOR is commutative, so 3 xor 2 xor 3 is the same as 3 xor 3 xor 2, which is 2
        """
        result = 0
        for num in nums:
            result ^= num
        return result