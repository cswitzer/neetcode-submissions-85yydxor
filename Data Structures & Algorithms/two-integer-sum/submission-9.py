class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = defaultdict(int)
        for i, num in enumerate(nums):
            comp[num] = i
        for i, num in enumerate(nums):
            comp_target = target - num
            if comp_target in comp and comp[comp_target] != i:
                return [i, comp[comp_target]]