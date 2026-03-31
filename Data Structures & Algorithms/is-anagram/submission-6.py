class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c_counts = defaultdict(int)
        for c in s:
            c_counts[c] += 1
        
        for c in t:
            if c_counts[c] == 0:
                return False
            c_counts[c] -= 1
        return True
