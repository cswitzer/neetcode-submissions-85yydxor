class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        longest = 0
        L = 0

        for R in range(len(s)):
            counts.update([s[R]])
            most_freq = counts.most_common(1)[0][1]
            while (R - L + 1) - most_freq > k:
                counts.subtract([s[L]])
                L += 1
            longest = max(longest, (R - L + 1))
        
        return longest