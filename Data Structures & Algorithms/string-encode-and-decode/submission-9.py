class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        i = 0

        while i < len(s):
            # j represents the right bound for 
            #   1. The number preceding every word (where i is the start)
            #   2. The end of a word (where i is the start)
            j = i
            while s[j] != '#':
                j += 1
            
            num_chars = int(s[i:j])
            i = j + 1
            j = i + num_chars

            result.append(s[i:j])
            i = j

        return result
