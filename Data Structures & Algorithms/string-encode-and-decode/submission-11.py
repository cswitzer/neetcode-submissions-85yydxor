class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            s_len = len(s)
            encoded += f"{s_len}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        decoded = []
        i = 0
        s_len = len(s)
        while i < s_len:
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            i = j + 1
            j = i + count
            decoded.append(s[i:j])
            i = j
        return decoded
