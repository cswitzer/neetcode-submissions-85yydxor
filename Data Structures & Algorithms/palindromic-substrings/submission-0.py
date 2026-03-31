class Solution:
    def countSubstrings(self, s: str) -> int:
        self.num_sub = 0
        
        def num_pal(left: int, right: int):
            """
            Treat i as center
            extend outwards if both chars are equal
            at each step, increment the number of palindromes
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.num_sub += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            num_pal(i, i)
            num_pal(i, i + 1)
        
        return self.num_sub