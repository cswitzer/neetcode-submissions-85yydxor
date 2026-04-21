class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        This solution does each of the 3 steps:

        1. Multiple individual digits
        2. Add product to result at i + j
        3. Propogate carry by adding it to i + j + 1 (the next greatest position)
        4. Keep only ones digit at i + j

        For this solution to work, we can reverse the input strings
        """

        if num1 == '0' or num2 == '0':
            return '0'
        
        res = [0 for _ in range(len(num1) + len(num2))]
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # The positions here are just like I did in grade school.
                # If i1 is at the first position, and i2 is at the 0 position,
                # then the resulting number should be placed in the 1st position
                # run through a simple example like 111 * 222 to jog your memory
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        
        # our answer is actually reversed at this point
        res, beg = res[::-1], 0

        # When reversing res back to what we want, remove all potential preceding zeroes
        while beg < len(res) and res[beg] == 0:
            beg += 1
        return "".join([str(num) for num in res[beg:]])