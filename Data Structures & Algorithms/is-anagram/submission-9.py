class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)
        for s_char, t_char in zip(s, t):
            s_counts[s_char] += 1
            t_counts[t_char] += 1

        for k in s_counts:
            if s_counts[k] != t_counts[k]:
                return False
        return True
        