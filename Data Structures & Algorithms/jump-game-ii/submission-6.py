class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        # This is like BFS since we are finding the minimum number of jumps,
        # going from level to level until we reach the end
        while r < len(nums) - 1:
            farthest = 0
            # we calculate the next level by getting the max index "farthest"
            # that we can reach within l and r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # update the new window
            l, r = r + 1, farthest
            res += 1
        
        return res