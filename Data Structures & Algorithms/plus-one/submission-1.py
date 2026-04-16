class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        99 becomes 100
        199 becomes 200
        109 becomes 110

        Anything that is not 9, we just increment the last digit by 1
        if digits only consists of 9's, the len of the result is len(digits) + 1, where 1 is followed by 0's
        
        In the case of 1099, the number of 9's is 2, so the 1 in 1100 must come after all 9's in position
        len(digits) and all 9's become 0's

        In the case of 109, the number of 9's is 1, so index 1 becomes "1" and all following 9's become 0's
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # if the input is 00, then the number is currently 00 according to the loop
        # all that is left is to account for the carried 1
        return [1] + digits
