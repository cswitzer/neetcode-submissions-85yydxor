class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            
            # 4#neet where i => 4 and j => #, so s[i:j] captures only 4
            num_chars = int(s[i:j])
            i = j + 1
            j = i + num_chars
            result.append(s[i:j])
            i = j
        
        return result
