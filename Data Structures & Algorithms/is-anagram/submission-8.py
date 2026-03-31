class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts_s = defaultdict(int)
        counts_t = defaultdict(int)
        for s_c, t_c in zip(s, t):
            counts_s[s_c] += 1
            counts_t[t_c] += 1
        
        return counts_s == counts_t