class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = Counter(s)
        t_counts = Counter(t)

        for c, counts in s_counts.items():
            if t_counts[c] != counts:
                return False
        
        return True