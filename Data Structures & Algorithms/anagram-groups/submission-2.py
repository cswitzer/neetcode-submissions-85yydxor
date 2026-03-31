class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            char_counts = [0] * 26
            for c in s:
                char_counts[ord(c) - ord('a')] += 1
            key = tuple(char_counts)
            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
        return anagrams.values()