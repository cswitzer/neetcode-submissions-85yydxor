class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_n1 = len(s1)
        len_n2 = len(s2)

        if len_n1 > len_n2:
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len_n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == s2_counts:
            return True

        # Now we continue where we left off at s1
        for i in range(len_n1, len_n2):
            # s1_counts will not change again, but we must keep updating s2_counts using
            # a fixed sliding window of length n1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - len_n1]) - ord('a')] -= 1

            if s1_counts == s2_counts:
                return True
        
        return False
