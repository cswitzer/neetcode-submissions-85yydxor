class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for s in strs:
            key = [0 for _ in range(26)]
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = str(key)
            ana_map[key].append(s)
        return [v for v in ana_map.values()]