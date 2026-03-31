class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [3,4,5,6,1,2]
        target => 1
        
        [3,4,5,6,1,2]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            # This means mid belongs to the left portion of the array
            if nums[left] <= nums[mid]:
                # target being greater than the mid could mean that the target is to the right
                # if target is 0 and mid is 6 in [3,4,5,6,0,1,2], how do we know to search the left or right
                # side? Well, target < nums[left] (0 < 3), so the target must be on the RIGHT
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # if the target is 4 and mid is 0 in [3,4,5,6,0,1,2], then the following is the case:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1            