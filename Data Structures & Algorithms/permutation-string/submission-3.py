class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts_s1 = [0 for _ in range(26)]
        counts_s2 = [0 for _ in range(26)]

        for c in s1:
            counts_s1[ord(c) - ord('a')] += 1
        
        for i in range(len(s1)):
            s2_c = s2[i]
            counts_s2[ord(s2_c) - ord('a')] += 1
        
        print(f"{counts_s1=} | {counts_s2=}")

        if counts_s1 == counts_s2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            counts_s2[ord(s2[r]) - ord('a')] += 1
            counts_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if counts_s1 == counts_s2:
                return True
            
        return False