class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            # This means mid belongs to the left portion of the array
            if nums[left] <= nums[mid]:
                # If the target sits between left and mid 
                # e.g. [3,4,5,6,7,0,1,2] where mid is 6 and target is 7,
                # where 3 <= 7 <= 6 is NOT true
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # If the target sits between mid and right
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1            