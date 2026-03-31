class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            char_counts = [0] * 26
            for c in s:
                char_counts[ord(c) - ord('a')] += 1
            key = tuple(char_counts)
            anagrams[key].append(s)
        return anagrams.values()