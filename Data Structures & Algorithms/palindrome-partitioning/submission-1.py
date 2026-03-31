class Solution:
    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        if not s or len(s) == 1:
            return True

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        path = []

        def dfs(start: int):
            # not len(path) == len(s), since s may be "aab" (len 3) and path is ["aa", "b"] (len 2)
            # 3 != 2, which means we would exclude the valid path above 
            if start == len(s):
                partitions.append(path[:])
                return
            
            # at the current index, only add and explore current paths for palindromes
            # e.g. babab
            # explore paths for either b, bab, or babab
            for end in range(start, len(s)):
                if self.is_palindrome(s, start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()
        
        dfs(0)
        return partitions