class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # if we can reach the goal from i, then we move the goal post since we know
            # i can reach the goal!
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0