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
        result = []
        len_digits = len(digits)

        nine_counts = 0
        for d in digits:
            if d == 9:
                nine_counts += 1

        if nine_counts == len_digits:
            return [1] + [0 for _ in range(len_digits)]

        result = [d for d in digits]

        # we only add by 1, so we only care if the very end does not have a 9
        if digits[-1] != 9:
            result[-1] += 1
            return result

        # There is a 9 at the end, so we must count backwards until arriving at the first non 9 digit
        # 10909 becomes 10910
        # 19999 becomes 20000
        # 999 becomes 1000, which is handled above already
        non_nine_index = 0
        for i in range(len(result) - 2, -1, -1):
            if result[i] != 9:
                non_nine_index = i
                result[non_nine_index] += 1
                break
        
        for i in range(non_nine_index + 1, len(result)):
            result[i] = 0
        
        return result
