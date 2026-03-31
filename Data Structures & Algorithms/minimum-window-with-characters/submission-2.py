class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        s_counts, t_counts = defaultdict(int), defaultdict(int)
        for c in t:
            t_counts[c] += 1
        
        have, seen = 0, len(t_counts)
        indices = [-1, -1]
        min_window = float("infinity")
        left = 0
        for right, c in enumerate(s):
            s_counts[c] += 1
            if c in t_counts and s_counts[c] == t_counts[c]:
                have += 1
            
            while have == seen:
                curr_window = right - left + 1
                if curr_window < min_window:
                    indices = [left, right]
                    min_window = curr_window
                
                if s[left] in t_counts:
                    s_counts[s[left]] -= 1
                    if s_counts[s[left]] < t_counts[s[left]]:
                        have -= 1
                left += 1
        
        left, right = indices
        return s[left:right + 1] if min_window != float("infinity") else ""
