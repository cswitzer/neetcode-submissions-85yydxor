class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) < len(t):
            return ""

        s_counts, t_counts = defaultdict(int), defaultdict(int)
        for c in t:
            t_counts[c] += 1
        
        indices, result = [-1, -1], float("infinity")
        have, need = 0, len(t_counts)
        l = 0
        for r, c in enumerate(s):
            s_counts[c] += 1
            if c in t_counts and s_counts[c] == t_counts[c]:
                have += 1

            # keep moving left pointer until the window no longer contains all the characters in t
            # this is really good because it allows us to shrink the window's length and find a new
            # potential min length
            while have == need:
                if r - l + 1 < result:
                    result = r - l + 1
                    indices = [l, r]

                s_counts[s[l]] -= 1
                if s[l] in t_counts and s_counts[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1
        
        left, right = indices
        return s[left:right + 1] if result != float("infinity") else ""