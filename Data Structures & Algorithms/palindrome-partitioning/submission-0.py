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
            if start == len(s):
                partitions.append(path[:])
                return
            
            for end in range(start, len(s)):
                if self.is_palindrome(s, start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()
        
        dfs(0)
        return partitions