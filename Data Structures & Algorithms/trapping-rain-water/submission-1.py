class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_l, max_r = height[0], height[right]
        area = 0

        while left < right:
            if max_l <= max_r:
                left += 1
                max_l = max(max_l, height[left])
                area += max_l - height[left]
            else:
                # notice here that max_l is definitely more than max_l,
                # so we can just say subtract the current height from max_r
                # without explicitly accounting for the left side
                right -= 1
                max_r = max(max_r, height[right])
                area += max_r - height[right]
        
        return area