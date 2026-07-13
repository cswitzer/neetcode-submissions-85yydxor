class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Take the window length and subtract by the count of the max character and compare > k
        This is how we calculate the max length
        """
        counts = defaultdict(int)
        l, longest = 0, 0
        for r, c in enumerate(s):
            counts[c] += 1

            # window len - most freq count = num replaced
            while ((r - l) + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        return longest

