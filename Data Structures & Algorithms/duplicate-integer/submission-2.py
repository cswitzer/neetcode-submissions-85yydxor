class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = set()
        for num in nums:
            if num not in existing:
                existing.add(num)
            else:
                return True
        return False    